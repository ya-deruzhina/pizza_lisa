from pizza_lisa.models import User, OrderModel, PizzaInOrder

from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect 

from admin_api.forms import ChangeStatusOrderForm
from admin_api.serializers import ChangeStatusSerializer

from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.views import APIView

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class OneOrderPageView(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # View One Order
    def get(self, request, order_id):
        try:
            user_order = OrderModel.objects.get(id=order_id)
        
        except Exception as exs:
            print ('Warming!!!', exs)  
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            pizza = PizzaInOrder.objects.filter(order_id=order_id)

            cost = 0
            for m in pizza:
                cost += m.count * m.price_one

            template = loader.get_template("orders/one_page_of_order.html")
            context = {
                "form":ChangeStatusOrderForm(),
                "user_order":user_order,
                "pizza":pizza,
                "cost":cost,

            }
            return HttpResponse(template.render(context,request))

    # Изменить статус заказа (+ если переводит в Архив, то добавляет к юзеру сумму заказа)
    def post(self, request, order_id):
        try:
            data = request.POST
            try:
                order = OrderModel.objects.get(id=order_id)
                user = User.objects.get(id = order.user_id)

            except Exception as exs:
                    print ('Warming!!!', exs)  
                    template = loader.get_template("main/page_404.html")
                    return HttpResponse(template.render())
            else:
                if OrderModel.objects.get(id=order_id).status != "ARCHIVE" and request.POST['status'] == "ARCHIVE":
                    user.total_shopping += order.total_money
                    user.save()
            
                if OrderModel.objects.get(id=order_id).status == "ARCHIVE" and request.POST['status'] != "ARCHIVE":
                    user.total_shopping -= order.total_money
                    user.save()
            instance = OrderModel.objects.get(pk=order_id)
            serializer = ChangeStatusSerializer (data=data,instance=instance)
            serializer.is_valid(raise_exception=True)

        except Exception as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        else:
            serializer.save()
            return HttpResponseRedirect ("")
