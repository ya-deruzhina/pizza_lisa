from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from pizza_lisa.models import CatalogModel

from admin_api.serializers import CatalogSerializer
from admin_api.forms import CreateCatalogForm

from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

from django.core.paginator import Paginator
from django.shortcuts import render

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class CatalogAdminView(APIView):
    # Страница со всеми сообщения + оставить новое
    permission_classes = [IsAdminUser]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self,request):
        catalog = CatalogModel.objects.all().order_by('name_pizza')
        count_pizza = len(catalog)
        template = loader.get_template("catalog/catalog_admin_all.html")
        context = {
            "catalog":catalog,
            "form":CreateCatalogForm(),
            "count_pizza":count_pizza,
        }
        return HttpResponse(template.render(context,request))
    
    # Создание новой пиццы
    def post(self,request):
        try:
            name_pizza = request.POST.get('name_pizza')
            ingredients = request.POST.get('ingredients')
            price = request.POST.get('price')
            price_disсont = request.POST.get('price_disсont')
            if price_disсont == None or price_disсont ==  '':
                price_disсont = 0.0
            amount = request.POST.get('amount')
            if amount == '' or amount == None:
                amount = 0

            data = {"name_pizza":name_pizza,"ingredients":ingredients,"price":price,"price_disсont":price_disсont,"amount":amount}
            serializer = CatalogSerializer(data=data)
            serializer.is_valid(raise_exception=True)
       
        except Exception as exs:
            print ('Warming!!!', exs)  
            template = loader.get_template("page_404_admin.html")
            return HttpResponse(template.render())
        
        else:
            serializer.save()
            return HttpResponseRedirect ("")


        

