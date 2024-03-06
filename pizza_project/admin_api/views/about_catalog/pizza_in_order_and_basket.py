from pizza_lisa.models import OrderModel, PizzaInOrder, BasketModel, CatalogModel

from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView


class PizzaInOrderAndBasketView(APIView):
    permission_classes = [IsAdminUser]
    # View Pizza in Basket and Orders ***
    def get(self, request, _id):
        try:
            name_pizza = CatalogModel.objects.get(id=_id).name_pizza

        except Exception as exs:
            print ('Warming!!!', exs)  
            template = loader.get_template("page_404_admin.html")
            return HttpResponse(template.render())

        else:
            pizza_in_basket = BasketModel.objects.filter(pizza = _id)
            orders_in_work = OrderModel.objects.exclude(status='ARCHIVE').exclude(status='CANCELED').order_by('order_time')

            number_working_orders = []
            users_in_order = {}

            for m in range(0, len(orders_in_work)):
                number_working_orders.append(orders_in_work[m].id)
                users_in_order [orders_in_work[m].id] = orders_in_work[m].user.username

            pizza_in_working_orders = {}

            for n in number_working_orders:
                pizza_in_working_orders[users_in_order[n]] = PizzaInOrder.objects.filter(pizza_id=_id).filter(order_id=n)
            
            pizza_in_working_orders = dict(filter(lambda x:x[1], pizza_in_working_orders.items()))


            template = loader.get_template("catalog/pizza_in_order.html")
            context = {
                "pizza_in_basket":pizza_in_basket,
                "pizza_in_working_orders":pizza_in_working_orders,
                "pizza_id":_id,
                "name_pizza":name_pizza,
            }
            return HttpResponse(template.render(context,request))  
    
class DeletePizzaFromBasketView(APIView):
    permission_classes = [IsAdminUser]
    # Delete Pizza from Basket ***
    def get(self, request, basket_id):
        try:
            basket = BasketModel.objects.get(id=basket_id)

        except Exception as exs:
            print ('Warming!!!', exs)  
            template = loader.get_template("page_404_admin.html")
            return HttpResponse(template.render())
    
        else:    
            id_pizza = basket.pizza.id
            basket.delete()
            return HttpResponseRedirect (f'/main/catalog/pizza/{id_pizza}/')    