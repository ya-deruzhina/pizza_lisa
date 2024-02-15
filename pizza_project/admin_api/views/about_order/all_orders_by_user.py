from pizza_lisa.models import User,OrderModel

from django.template import loader
from django.http import HttpResponse 

from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView


class OrdersByUserView(APIView):
    permission_classes = [IsAdminUser]
    # Страница со всеми заказами кроме в архиве + отмененные
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        
        except Exception as exs:
            print ('Warming!!!', exs)  
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            user_orders = OrderModel.objects.filter(user_id = user_id).exclude(status='ARCHIVE').exclude(status='CANCELED').order_by('order_time')
            count_orders = len(user_orders)


            template = loader.get_template("orders/all_orders_by_user.html")
            context = {
                "user": user,
                "count_orders":count_orders,
                "user_orders":user_orders,
            }
            return HttpResponse(template.render(context,request)) 
    
class OrdersByUserArchiveView(APIView):
    permission_classes = [IsAdminUser]
    # Страница со времи заказами в архиве + отмененные
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        
        except Exception as exs:
            print ('Warming!!!', exs)  
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            user_orders = OrderModel.objects.filter(user_id = user_id).exclude(status='NEW').exclude(status='COOKING').exclude(status='TASTING').exclude(status='PACKING').exclude(status='IN_DELIVERY').order_by('order_time')
            count_orders = len(user_orders)

            template = loader.get_template("orders/all_orders_by_user.html")
            context = {
                "user": user,
                "count_orders":count_orders,
                "user_orders":user_orders,
            }
            return HttpResponse(template.render(context,request)) 

