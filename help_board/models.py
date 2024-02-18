from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    fontawesome_icon = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hm_categories"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"


class Query(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=False, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hm_queries"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="query_category"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Answer(models.Model):
    query = models.ForeignKey(
        Query, on_delete=models.CASCADE, related_name="query_asked"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="answered_by"
    )
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.content}"
