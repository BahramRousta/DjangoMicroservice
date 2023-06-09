import requests
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=500,
                             db_index=True)
    slug = models.SlugField(max_length=500,
                            unique=True)
    image = models.ImageField(upload_to='images',
                              blank=True,
                              null=True)
    published = models.DateField(auto_now=False,
                                 auto_now_add=False)
    category_id = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    new_publish = models.BooleanField(default=False, null=True, blank=True)
    available = models.BooleanField(default=True, null=True, blank=True)
    count_sold = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['-published']
        index_together: (('id', 'slug'),)

    def __str__(self):
        return self.title

    @property
    def category(self):
        # Retrieve the category object from the category microservice using its ID
        response = requests.get(f'http://category-microservice/categories/{self.category_id}/')
        if response.status_code == 200:
            return response.json()
        return None
