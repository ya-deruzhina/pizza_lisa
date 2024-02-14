from django.db import models
from pizza_lisa.models import User, CatalogModel
from datetime import datetime


class OrderModel(models.Model):
    NEW = "NEW"
    COOKING = "COOKING"
    TASTING = "TASTING"
    PACKING = "PACKING"
    IN_DELIVERY = "IN_DELIVERY"
    ARCHIVE = "ARCHIVE"
    CANCELED = "CANCELED"

    STATUS_ORDER = [
    (NEW, "NEW"),
    (COOKING, "COOKING"),
    (TASTING, "TASTING"),
    (PACKING, "PACKING"),
    (IN_DELIVERY, "IN_DELIVERY"),
    (ARCHIVE, "ARCHIVE"),
    (CANCELED,"CANCELED"),
    ]

    order_time = models.DateTimeField(auto_now_add = True, null = True)
    status = models.CharField (choices=STATUS_ORDER, default=NEW)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(null = False)
    phone = models.BigIntegerField(null = False)
    address = models.TextField(default = "Self-pickup")
    comment = models.TextField(null = True, default = 'Order without Comment') 

    def __str__(self):
        return self.status
    
class PizzaInOrder (models.Model):
    order = models.ForeignKey(OrderModel, null=False, on_delete=models.CASCADE)
    pizza = models.ForeignKey (CatalogModel, null=False, on_delete=models.CASCADE)
    count = models.IntegerField()
    price_one = models.FloatField(null = False)

    def serilize_from_db (self):
        return {'id':self.id, 'order':self.order,'pizza':self.pizza,'count':self.count,'price_one':self.price_one}

