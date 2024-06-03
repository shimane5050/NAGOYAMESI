from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=20)
    name_kana = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name