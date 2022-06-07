from django.shortcuts import render, redirect
from .models import BlogPost
from .models import BlogPostUser
from .models import UserBlocked
from .forms import AddPostForm, BlockForm
from .admin import UserBlockedAdmin


# Create your views here.


def posts(request):
    all_posts = []
    try:
        user = BlogPostUser.objects.get(user=request.user)
        blocked = UserBlocked.objects.filter(user_account=user).all()
        list_posts = BlogPost.objects.all()
        for p in list_posts:
            for b in blocked:
                if p.user.user.username == b.user_account.user.username:
                    continue
                all_posts.append(p)
    except BlogPostUser.DoesNotExist:
        ...
    context = {"posts": all_posts, }
    return render(request, 'posts.html', context=context)


def addPost(request):
    if request.method == "POST":
        data_post = AddPostForm(data=request.POST, files=request.FILES)
        if data_post.is_valid():
            blogPost = data_post.save(commit=False)
            blogPost.user = BlogPostUser.objects.get(user=request.user)
            blogPost.save()
            return redirect("profileUser/")
    context = {"form": AddPostForm, }
    return render(request, 'addPost.html', context=context)


def profile_user(request):
    user_current = BlogPostUser.objects.get(user=request.user)
    posts_user = BlogPost.objects.filter(user=user_current).all()
    context = {"user": user_current, "posts_user": posts_user, }
    return render(request, 'profileUser.html', context=context)


def blockedUsers(request):
    if request.method == "POST":
        data_post = BlockForm(data=request.POST, files=request.FILES)
        if data_post.is_valid():
            users_data = data_post.save(commit=False)
            users_data.user_account = BlogPostUser.objects.get(user=request.user)
            users_data.save()
            return redirect("blockedUsers")
    user = BlogPostUser.objects.get(user=request.user)
    blocked_list = UserBlocked.objects.filter(user_account=user).all()
    context = {"blocked_list": blocked_list, "formBlock": BlockForm, }
    return render(request, 'blockedUsers.html', context=context)

