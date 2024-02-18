from django.http import HttpResponse
from django.template import loader

from pizza_lisa.models import OrderModel, PizzaInOrder

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class OneOrdersUserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request, order_id):
        try:
            order = OrderModel.objects.get(id=order_id)
                
        except Exception  as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:        
            all_pizza = PizzaInOrder.objects.filter(order=order_id)
            one_pizza_in_order = {}
            all_price = round(order.total_money,2)
            for m in range(0,(len(all_pizza))):
                one_pizza_name = all_pizza [m].pizza
                one_pizza_count = all_pizza[m].count
                one_pizza = {"pizza":one_pizza_name, "count":one_pizza_count}
                one_pizza_in_order[m] = one_pizza
                order_time = order.order_time.strftime("%H:%M:%S - %d.%m.%Y ")
                
                pizza = {
                    "id":order.id,
                    "order_time": order_time,
                    "comment": order.comment,
                    "status": order.status,
                    "name": order.name, 
                    "phone": order.phone,
                    "all_price":all_price,
                    "address":order.address,
                    "one_pizza_in_order":one_pizza_in_order,
                    }      
            count_pizza = one_pizza_in_order.keys()
            if order.status == 'NEW':
                template = loader.get_template("order/one_order.html")
                context = {
                    "pizza":pizza,
                    "count_pizza":count_pizza,
                }
                return HttpResponse(template.render(context,request))
        
            else:
                template = loader.get_template("order/one_order_const.html")
                context = {
                    "pizza":pizza,
                    "count_pizza":count_pizza,
                }
                return HttpResponse(template.render(context,request))