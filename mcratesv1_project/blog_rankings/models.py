from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=256)
    url = models.URLField()
    views = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title
