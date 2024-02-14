from django.db import models

class CatalogModel(models.Model):
    name_pizza = models.CharField(null = False)
    ingredients = models.TextField(null = False)
    price = models.FloatField(null = False)
    price_disсont = models.FloatField(null=True,default = 0)

    def __str__(self):
        return self.name_pizza