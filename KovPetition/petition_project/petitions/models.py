from django.db import models
from django.contrib.auth.models import User


class Petition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    supporters = models.ManyToManyField(User, related_name='supported_petitions', blank=True)

    def __str__(self):
        return self.title

    def count_supporters(self):
        return self.supporters.count()
