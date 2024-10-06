from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    author = models.ForeignKey(Author,related_name='books', on_delete=models.CASCADE)