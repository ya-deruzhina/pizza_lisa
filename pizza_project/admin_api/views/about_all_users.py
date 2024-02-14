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

class AboutAllUersPageView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        users = User.objects.all().order_by('username')
        about_user = {}

        # Подсчет сообщений со статусом новый по пользователю
        for id in users:
            message = MessagesModel.objects.filter(new = True)
            count_messages = len(message.filter(user_page_id=id))

            new_orders = OrderModel.objects.filter(status='NEW')
            count_orders = len(new_orders.filter(user_id=id))

            about_user[id]  = {'new_message':count_messages, 'new_orders':count_orders}


        done_orders = OrderModel.objects.filter(status='ARCHIVE')
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

        # import pdb; pdb.set_trace()

        template = loader.get_template("about_user/about_all_users.html")
        context = {
            "users": users,
            "about_user":about_user,
            "price":price,

        }
        return HttpResponse(template.render(context,request))    