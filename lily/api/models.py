from django.db import models

# Create your models here.
class WikiKnowledge(models.Model):
    url = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    summary = models.TextField()
    lang = models.CharField(max_length=15)


class Query(models.Model):
    name = models.CharField(max_length=255, unique=True)
    wiki = models.ForeignKey(WikiKnowledge, on_delete=models.CASCADE)

