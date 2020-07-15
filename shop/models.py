from django.db import models


class Category(models.Model):
    name = models.CharField(max_lenght=250)
    friendly_name = models.CharField(max_lenght=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
