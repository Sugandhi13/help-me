from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100,blank=True,unique=True)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,blank=True,unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hm_user"
    )
    describe_yourself = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
