from pizza_lisa.models import OrderModel, PizzaInOrder, BasketModel, CatalogModel,User

from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

class DeletePizzaFromOrderView(APIView):
    permission_classes = [IsAdminUser]
    # Delete Pizza from Orders ***
    def get(self, request, pizza_id):
        try:
            pizza_in_order = PizzaInOrder.objects.get(id=pizza_id)
            order_id = pizza_in_order.order_id
            order = OrderModel.objects.get(id=order_id)

        except Exception as exs:
            print ('Warming!!!', exs)  
            template = loader.get_template("page_404_admin.html")
            return HttpResponse(template.render())

        else:        
            order.total_money -= round((pizza_in_order.price_one),2)
            order.save()
            pizza_in_order.count -= 1
            if pizza_in_order.count == 0:
                pizza_in_order.delete()
            else:
                pizza_in_order.save()

            return HttpResponseRedirect (f'/main/user/orders/{order_id}/')