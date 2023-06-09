from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
