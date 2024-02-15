from pizza_lisa.models import OrderModel, PizzaInOrder,CatalogModel, ReviewModel, BasketModel

from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect 

from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.views import APIView

from admin_api.forms import UpdateCatalogForm
from admin_api.serializers import UpdateCatalogSerializer



class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class PizzaOneView(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    # View Pizza
    def get(self, request, _id):
        try:
            catalog = CatalogModel.objects.get(id=_id)
        
        except Exception as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            template = loader.get_template("catalog/catalog_one_admin.html")
            context = {
                "catalog":catalog,
                "form": UpdateCatalogForm(),
            }
            return HttpResponse(template.render(context,request))  
    
    
    # Change Pizza
    def post(self, request, _id):
        try:
            data = request.POST
            instance = CatalogModel.objects.get(pk=_id)
            serializer = UpdateCatalogSerializer (data=data,instance=instance)
            serializer.is_valid(raise_exception=True)

        except Exception as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        else:
            serializer.save()
            return HttpResponseRedirect ("")
 

 # Delete Pizza
class PizzaAdminDelete (APIView):
    permission_classes = [IsAdminUser]
    def get (self, request,_id):
        try:
            catalog = CatalogModel.objects.get(id=_id)
    
        except Exception  as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            review = ReviewModel.objects.filter(pizza_id=_id)
            pizza = PizzaInOrder.objects.filter(pizza_id=_id)
            basket = BasketModel.objects.filter(pizza_id=_id)
            orders_in_work = OrderModel.objects.exclude(status='CANCELED').exclude(status='ARCHIVE')

            number_orders = []

            for m in (0, len(orders_in_work)-1):
                number_orders.append(orders_in_work[m].id)

            for n in number_orders:
                if len (pizza.filter(order_id=n)) > 0:
                    print ('Warming!!! Pizza In Order', )   
                    template = loader.get_template("main/page_404.html")
                    return HttpResponse(template.render())

            catalog.delete()
            review.delete()
            pizza.delete()
            basket.delete()
            
            return HttpResponseRedirect ("/main/catalog/")