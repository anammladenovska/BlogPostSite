from django.contrib import admin
from .models import BlogPostUser, BlogPost, BlogPostFile, Comment, UserBlocked
from rangefilter.filters import DateTimeRangeFilter
from django.db.models import Q


# Register your models here.

class BlogPostUserAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj is not None and request.user == obj.user:
            return True
        return False


admin.site.register(BlogPostUser, BlogPostUserAdmin)


class CommentBlogPostAdmin(admin.StackedInline):
    list_display = ("content",)
    model = Comment
    extra = 0
    exclude = ("user",)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "user")
    search_fields = ("title", "content")
    exclude = ("user",)
    list_filter = (("date_created", DateTimeRangeFilter),)
    inlines = [CommentBlogPostAdmin]

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        user = BlogPostUser.objects.get(user=request.user)
        blocked_users = UserBlocked.objects.filter(user_account=user).all()
        for bu in blocked_users:
            if obj is not None and obj.user == bu:
                return False
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        return True

    def save_model(self, request, obj, form, change):
        author_user = BlogPostUser.objects.get(user=request.user)
        obj.user = author_user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        author_user = BlogPostUser.objects.get(user=request.user)
        if obj is not None and author_user == obj.user:
            return True
        return False


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogPostFile)


class UserBlockedAdmin(admin.ModelAdmin):
    list_display = ("user_blocked",)
    exclude = ("user_account",)

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        user = BlogPostUser.objects.get(user=request.user)
        if obj and obj.user_account == user:
                return True
        return False

    def get_queryset(self, request):
        user = BlogPostUser.objects.get(user=request.user)
        return UserBlocked.objects.filter(user_account=user).all()

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        user = BlogPostUser.objects.get(user=request.user)
        if obj and obj.user_account == user:
            return True
        return False

    def has_add_permission(self, request):
        return True

    def save_model(self, request, obj, form, change):
        author_user = BlogPostUser.objects.get(user=request.user)
        obj.user_account = author_user
        super().save_model(request, obj, form, change)


admin.site.register(UserBlocked, UserBlockedAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", )
    search_fields = ("content", )
    exclude = ("user", )

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        author_user = BlogPostUser.objects.get(user=request.user)
        if obj is not None and (obj.user == author_user):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        author_user = BlogPostUser.objects.get(user=request.user)
        if obj is not None and (obj.user == author_user):
            return True
        return False

    def has_add_permission(self, request):
        return True

    def save_model(self, request, obj, form, change):
        author_user = BlogPostUser.objects.get(user=request.user)
        obj.user = author_user
        super().save_model(request, obj, form, change)


admin.site.register(Comment, CommentAdmin)
