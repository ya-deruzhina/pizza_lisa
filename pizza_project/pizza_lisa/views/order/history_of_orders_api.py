from django.http import HttpResponse
from django.template import loader

from pizza_lisa.models import OrderModel, PizzaInOrder

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class OrdersUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    # Соединяю модели OrderModel и PizzaInOrder по номеру заказа
    def get(self,request):        
        orders_with_pizza = OrderModel.objects.filter(user=request.user.id).order_by('-order_time')
        pizza_in_order = {}

        for n in range (0,(len(orders_with_pizza))) :
            pizza_in_order[orders_with_pizza[n].id] = PizzaInOrder.objects.filter(order=orders_with_pizza[n].id)

        numbers_orders = pizza_in_order.keys()

        order = {}
        for i in numbers_orders:
            try:
                orders = OrderModel.objects.get (id = i)
                all_price = orders_with_pizza.get(id=i).total_money            
                    
            except Exception  as exs:
                print ('Warming!!!', exs)   
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render())
            
            else:
                order_time = orders.order_time.strftime("%H:%M:%S - %d.%m.%Y ")
                pizza = {
                    "status": orders.status,
                    "order_time": order_time,
                    "all_price":all_price,
                    }      
                order [i] = (pizza)

        template = loader.get_template("order/history_orders.html")
        context = {
            "order":order,
            "numbers_orders":numbers_orders,
        }
        return HttpResponse(template.render(context,request))