from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class BlogPostUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    surname = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    interests = models.TextField(max_length=500, null=True, blank=True)
    skills = models.TextField(max_length=500, null=True, blank=True)
    profession = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(BlogPostUser, on_delete=models.CASCADE, null=False)
    content = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    last_changes = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " " + self.content


class BlogPostFile(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=False)
    file = models.FileField()


class Comment(models.Model):
    content = models.TextField(max_length=1000)
    user = models.ForeignKey(BlogPostUser, on_delete=models.CASCADE, null=False)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.content


class UserBlocked(models.Model):
    user_account = models.ForeignKey(BlogPostUser, on_delete=models.CASCADE, null=False, related_name="wants_to_block")
    user_blocked = models.ForeignKey(BlogPostUser, on_delete=models.CASCADE, null=False, related_name="blocked")

