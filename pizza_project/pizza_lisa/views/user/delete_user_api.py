from django.http import HttpResponseRedirect,HttpResponse
from django.db import transaction
from django.template import loader
from rest_framework.permissions import IsAuthenticated

from pizza_lisa.models import User,BasketModel, MessagesModel,OrderModel, ReviewModel, PizzaInOrder
from rest_framework.views import APIView

# Delete
class UserDeleteView (APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request):
        with transaction.atomic():
            basket_of_user = BasketModel.objects.filter(user=request.user.id)
            basket_of_user.delete()
            
            message_of_user = MessagesModel.objects.filter(user_page=request.user.id)
            message_of_user.delete()

            order_of_user = OrderModel.objects.filter(user=request.user.id)
            if len(order_of_user.exclude(status = "NEW").exclude(status="CANCELED").exclude(status ="ARCHIVE"))>0:
                return HttpResponseRedirect ("/pizza/lisa/user_orders/")
    
            if len (order_of_user) > 0:
                number_of_order = []

                for n in range (0,(len(order_of_user))) :
                    number_of_order.append (order_of_user[n].id)

                for m in number_of_order:
                    pizza = PizzaInOrder.objects.filter(order = m)
                    pizza.delete()

            order_of_user.delete()

            review_of_user = ReviewModel.objects.filter(user=request.user.id)
            review_of_user.delete()
            

            try:
                user = User.objects.get(id=request.user.id)

            except Exception as exs:
                print ('Warming!!!', exs)   
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render())

            else:
                user.delete()
                return HttpResponseRedirect ("/pizza/sign_in/logout/")
        

