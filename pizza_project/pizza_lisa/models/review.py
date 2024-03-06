from django.db import models
from pizza_lisa.models import User, CatalogModel

class ReviewModel(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    pizza = models.ForeignKey(CatalogModel, null=False, on_delete=models.CASCADE)
    review = models.TextField(null = False)
    time = models.TimeField(auto_now_add = True)

    def __str__(self):
        return self.review