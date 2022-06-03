from django.db import models
from django.shortcuts import resolve_url

from accounts.models import Profile


class Bookmark(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10)
    url = models.URLField()

    def __str__(self):
        # return self.name + " : " + self.url  # 어무해 : https://bit.ly/2022NP
        return f'{self.name} : {self.url}'

    def get_absolute_url(self):
        return resolve_url('bookmark:detail', pk=self.pk)