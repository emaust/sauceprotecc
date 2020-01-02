from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100)
    avatar = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    social_media = models.CharField(max_length=400, null=True, blank=True)

    class Meta:
        ordering = ["username", "name", "email", "social_media"]

    def __str__(self):
        return 

class Image(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True, blank=True)
    date_posted = models.DateTimeField()
    post_location = models.URLField
    whitelist = models.URLField()

    class Meta:
        ordering = ["user", "description", "file_name", "date_posted", "whitelist"]

    def __str__(self):
        return self.file_name

class Flagged(models.Model):
    images = models.ManyToManyField(Image)
    name = models.CharField(max_length=150)
    url = models.URLField()

    def __str__(self):
        return self.name