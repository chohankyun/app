from django.db import models

from backend.api.uauth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    priority = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subject = models.CharField(max_length=300, blank=False)
    content = models.TextField(blank=False)
    text_content = models.CharField(max_length=20000, blank=True)
    first_image_source = models.CharField(max_length=500, blank=True)
    click_count = models.IntegerField()
    reply_count = models.IntegerField()
    recommend_count = models.IntegerField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    text_content = models.CharField(max_length=20000, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reply'


class Recommend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recommend'
