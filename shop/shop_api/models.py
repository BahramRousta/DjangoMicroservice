from django.db import models


class Shop(models.Model):

    title = models.CharField(max_length=250)
    owner_id = models.IntegerField()

    def __str__(self):
        return self.title

