from django.http import HttpResponse
from django.template import loader

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from pizza_lisa.models import CatalogModel

class CatalogDiscontView(APIView):
    # Выводит акционные товары
    permission_classes = [IsAuthenticated]
    def get(self,request):
        # __gt значит больше
        catalog = CatalogModel.objects.filter(price_disсont__gt=0).filter(amount__gt=0).order_by('name_pizza')
        template = loader.get_template("catalog/catalog_discont.html")
        context = {
            "catalog":catalog,
        }
        return HttpResponse(template.render(context,request))