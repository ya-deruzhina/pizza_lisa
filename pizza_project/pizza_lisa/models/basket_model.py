from django.db import models
from pizza_lisa.models.user_model import User
from pizza_lisa.models.catalog_model import CatalogModel

class BasketModel (models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    pizza = models.ForeignKey(CatalogModel, null=False, on_delete=models.CASCADE)
    count = models.IntegerField (null=False)