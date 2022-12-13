from django.db import models


class Author(models.Model):
    salutation = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author', null=True, blank=True)