from pizza_lisa.models import User, MessagesModel,OrderModel, PizzaInOrder

from django.http import HttpResponse
from django.template import loader

from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

class FirstAdminPageView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        users = User.objects.all().order_by('username')
        about_user = {}
        new_message = MessagesModel.objects.filter(new = True)
        new_orders = OrderModel.objects.filter(status='NEW')
        
        # Подсчет сообщений со статусом новый по пользователю
        for id in users:   
            count_messages = len(new_message.filter(user_page_id=id))
            count_orders = len(new_orders.filter(user_id=id))
            about_user[id]  = {'new_message':count_messages, 'new_orders':count_orders}

        price = 0
        for byn in range(0,len(users)):
            price += users[byn].total_shopping
            
        template = loader.get_template("first_page_admin.html")
        context = {
            "users": users,
            "about_user":about_user,
            "price":price,
            "new_message":new_message,
            "new_orders": new_orders,

        }
        return HttpResponse(template.render(context,request))    