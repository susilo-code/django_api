from django.db import models

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Album(models.Model):
    artist = models.TextField()
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Report(models.Model):
    author = models.TextField()
    topic = models.CharField(max_length=100)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    num_pages = models.IntegerField()

    def __str__(self):
        return self.content
