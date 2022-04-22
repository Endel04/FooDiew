from django.db import models

class Bookmark(models.Model):
    name = models.CharField(max_length=10)
    url = models.URLField()

    def __str__(self):
        # return self.name + " : " + self.url  # 어무해 : https://bit.ly/2022NP
        return f'{self.name} : {self.url}'