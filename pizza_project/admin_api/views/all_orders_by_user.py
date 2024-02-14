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

from admin_api.forms import ChangeStatusOrderForm,UserForm
from pizza_lisa.models import User
from admin_api.serializers import ChangeStatusSerializer,ChangeDiscontSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.views import APIView


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class OrdersByUserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        user_orders = OrderModel.objects.filter(user_id = user_id).exclude(status='ARCHIVE').exclude(status='CANCELED').order_by('order_time')
        count_orders = len(user_orders)

        done_orders = OrderModel.objects.filter(status='ARCHIVE')

        price = 0
        number_orders = []
        for count in range (0,len(done_orders)):
            for_pizza_price = done_orders[count].id
            number_orders.append(for_pizza_price)
        # import pdb; pdb.set_trace()
        for numb in number_orders:
            pizza = PizzaInOrder.objects.filter(order_id = numb)
            for one_pizza in range (0,len(pizza)):
                count_one = pizza[one_pizza].count
                price_one = pizza[one_pizza].price_one
                price += count_one * price_one


        template = loader.get_template("about_user/all_orders_by_user.html")
        context = {
            "user": user,
            "count_orders":count_orders,
            "user_orders":user_orders,
            "price":price,
        }
        # import pdb; pdb.set_trace()
        return HttpResponse(template.render(context,request)) 
    
class OrdersByUserArchiveView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        user_orders = OrderModel.objects.filter(user_id = user_id).exclude(status='NEW').exclude(status='COOKING').exclude(status='TASTING').exclude(status='PACKING').exclude(status=' IN_DELIVERY').order_by('order_time')
        count_orders = len(user_orders)

        done_orders = user_orders.filter(status='ARCHIVE')

        price = 0
        number_orders = []
        for count in range (0,len(done_orders)):
            for_pizza_price = done_orders[count].id
            number_orders.append(for_pizza_price)
        # import pdb; pdb.set_trace()
        for numb in number_orders:
            pizza = PizzaInOrder.objects.filter(order_id = numb)
            for one_pizza in range (0,len(pizza)):
                count_one = pizza[one_pizza].count
                price_one = pizza[one_pizza].price_one
                price += count_one * price_one


        template = loader.get_template("about_user/all_orders_by_user.html")
        context = {
            "user": user,
            "count_orders":count_orders,
            "user_orders":user_orders,
            "price":price,
        }
        # import pdb; pdb.set_trace()
        return HttpResponse(template.render(context,request)) 

