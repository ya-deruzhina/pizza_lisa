# cont_pazza - len(Catalog)
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from pizza_lisa.models import MessagesModel, CatalogModel, ReviewModel, PizzaInOrder, BasketModel
from admin_api.serializers import CatalogSerializer
from admin_api.forms import CreateCatalogForm

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class CatalogAdminView(APIView):
    # Страница со всеми сообщения + оставить новое
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self,request):
        # username = 'admin'
        catalog = CatalogModel.objects.all().order_by('name_pizza')
        count_pizza = len(catalog)
        template = loader.get_template("catalog/catalog_admin_all.html")
        context = {
            "catalog":catalog,
            "form":CreateCatalogForm(),
            "count_pizza":count_pizza,
        }
        return HttpResponse(template.render(context,request))
    
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

# Delete message
class PizzaAdminDelete (APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request,_id):
        try:
            catalog = CatalogModel.objects.get(id=_id)
            review = ReviewModel.objects.filter(pizza_id=_id)
            orders = PizzaInOrder.objects.filter(pizza_id=_id)
            basket = BasketModel.objects.filter(pizza_id=_id)
        
        except Exception  as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            catalog.delete()
            review.delete()
            orders.delete()
            basket.delete()
            
            return HttpResponseRedirect ("/main/catalog/")
