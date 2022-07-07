from django.db import models
from django.shortcuts import resolve_url

from accounts.models import Profile


class Food(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return resolve_url('food:detail', pk=self.pk)