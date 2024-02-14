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


class AdminAboutUserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        user_message = MessagesModel.objects.filter(user_page_id=user_id)
        count_new_message = len(user_message.filter(new = True))
        user_orders = OrderModel.objects.filter(user_id = user_id)
        new_orders = user_orders.filter(status = "NEW").order_by('order_time')
        count_new_orders = len(new_orders)

        done_orders = OrderModel.objects.filter(status='ARCHIVE').filter(user=user.id)
        price = 0
        number_orders = []
        for count in range (0,len(done_orders)):
            for_pizza_price = done_orders[count].id
            number_orders.append(for_pizza_price)

        for numb in number_orders:
            pizza = PizzaInOrder.objects.filter(order_id = numb)
            for one_pizza in range (0,len(pizza)):
                count_one = pizza[one_pizza].count
                price_one = pizza[one_pizza].price_one
                price += count_one * price_one


        template = loader.get_template("about_user/admin_about_user.html")
        context = {
            "user": user,
            "count_new_message":count_new_message,
            "count_new_orders":count_new_orders,
            "new_orders":new_orders,
            "price":price,
            "form": UserForm(),
        }
        return HttpResponse(template.render(context,request))  

    def post(self, request, user_id):
        try:
            data = request.POST
            instance = User.objects.get(pk=user_id)
            serializer = ChangeDiscontSerializer(data=data,instance=instance)
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
 