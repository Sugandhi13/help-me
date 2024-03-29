# Importing libraries required to build models

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Defining constant variable status
STATUS = ((0, "Draft"), (1, "Published"))


# Create Category model
class Category(models.Model):
    """
    Stores single category request to :model:`auth.User`.
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    fontawesome_icon = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hm_categories"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"


# Create Query model
class Query(models.Model):
    """
    Stores single query request to :model:`auth.User`
    and `help_board.Category`.
    """
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

    # Create query slug using title input from the user
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


# Create Answer model
class Answer(models.Model):
    """
    Stores single answer request to :model:`auth.User`
    and `help_board.Query`.
    """
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
