from django.http import HttpResponse
from django.template import loader

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from pizza_lisa.models import CatalogModel

class CatalogView(APIView):
    # Выводит все товары из БД
    permission_classes = [IsAuthenticated]
    def get(self,request):
        catalog_discont = CatalogModel.objects.filter(price_disсont__gt=0).filter(amount__gt=0).order_by('name_pizza')
        catalog = CatalogModel.objects.filter(price_disсont=0).filter(amount__gt=0).order_by('name_pizza')
        template = loader.get_template("catalog/catalog.html")
        context = {
            "catalog":catalog,
            "catalog_discont":catalog_discont,
        }
        return HttpResponse(template.render(context,request))