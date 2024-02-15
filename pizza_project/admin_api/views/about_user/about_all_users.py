from pizza_lisa.models import User, MessagesModel,OrderModel, PizzaInOrder

from django.template import loader
from django.http import HttpResponse

from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

class AboutAllUersPageView(APIView):
    permission_classes = [IsAdminUser]
    # Страница со всеми пользователями
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

        price = 0
        for byn in range(0,len(users)):
            price += users[byn].total_shopping

        template = loader.get_template("about_user/about_all_users.html")
        context = {
            "users": users,
            "about_user":about_user,
            "price":price,

        }
        return HttpResponse(template.render(context,request))    