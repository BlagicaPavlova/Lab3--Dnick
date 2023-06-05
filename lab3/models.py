from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Post(models.Model):
        title = models.CharField(max_length=255)
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        last_modified = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

class Comment(models.Model):
            post = models.ForeignKey(Post, on_delete=models.CASCADE)
            author = models.ForeignKey(User, on_delete=models.CASCADE)
            content = models.TextField()
            created_at = models.DateTimeField(auto_now_add=True)

            def __str__(self):
                return f"{self.content} - {self.created_at}"