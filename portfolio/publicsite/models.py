from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False)


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)


class PostView(models.Model):
    view_date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
