from django.db import models

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=40)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=350)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True,related_name="posts")
    tags = models.ManyToManyField(Tag)


