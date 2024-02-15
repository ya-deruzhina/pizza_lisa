from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from pizza_lisa.models import CatalogModel

from admin_api.serializers import CatalogSerializer
from admin_api.forms import CreateCatalogForm

from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

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
            serializer = CatalogSerializer(data=request.POST)
            serializer.is_valid(raise_exception=True)
       
        except Exception as exs:
            print ('Warming!!!', exs)  
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            serializer.save()
            return HttpResponseRedirect ("")


        

