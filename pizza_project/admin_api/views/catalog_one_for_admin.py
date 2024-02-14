from pizza_lisa.models import User, MessagesModel,OrderModel, PizzaInOrder

from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect 
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse

from pizza_lisa.forms import UpdateUserForm 
from pizza_lisa.models import User
from pizza_lisa.serializers import UserUpdateSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.views import APIView

from admin_api.forms import ChangeStatusOrderForm,UserForm

from pizza_lisa.models import User, MessagesModel,OrderModel, PizzaInOrder

from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect 
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse

from admin_api.forms import ChangeStatusOrderForm,UserForm,UpdateCatalogForm
from pizza_lisa.models import User
from admin_api.serializers import ChangeStatusSerializer,ChangeDiscontSerializer,UpdateCatalogSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.views import APIView

from pizza_lisa.models import MessagesModel, CatalogModel, ReviewModel, PizzaInOrder, BasketModel

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class PizzaOneView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self, request, _id):
        catalog = CatalogModel.objects.get(id=_id)

        template = loader.get_template("catalog/catalog_one_admin.html")
        # import pdb; pdb.set_trace()
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
            # import pdb; pdb.set_trace()
            serializer.is_valid(raise_exception=True)

        except Exception as exs:
            # import pdb; pdb.set_trace()
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
            pizza = PizzaInOrder.objects.filter(pizza_id=_id)
            basket = BasketModel.objects.filter(pizza_id=_id)
            orders_in_work = OrderModel.objects.exclude(status='CANCELED').exclude(status='ARCHIVE')

            number_orders = []

            for m in (0, len(orders_in_work)-1):
                number_orders.append(orders_in_work[m].id)

            for n in number_orders:
                if len (pizza.filter(pizza_id=_id)) > 0:
                    print ('Warming!!! Pizza In Order', )   
                    template = loader.get_template("main/page_404.html")
                    return HttpResponse(template.render())
        
        except Exception  as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            catalog.delete()
            review.delete()
            pizza.delete()
            basket.delete()
            
            return HttpResponseRedirect ("/main/catalog/")