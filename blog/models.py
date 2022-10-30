from django.db import models
from django.conf import settings
#from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    tex = models.TextField()
    created_data = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.published_date = models.DateTimeField(auto_now_add=True)
        self.save()

    def __str__(self):
        return self.title
