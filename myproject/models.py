from django.db import models

class Article(models.Model):
    image = models.URLField()
    date = models.CharField(max_length=10, default="2023/06/12")
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
