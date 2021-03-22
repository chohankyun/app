from django.db import models


class Category(models.Model):
    code = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=100, blank=False)
    priority = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
