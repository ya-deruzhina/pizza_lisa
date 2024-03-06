from pizza_lisa.models import User,OrderModel

from django.template import loader
from django.http import HttpResponse 

from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView


class AllOrdersView(APIView):
    permission_classes = [IsAdminUser]
    # Страница со всеми заказами
    def get(self, request):
        orders = OrderModel.objects.all().order_by('id')
        count_orders = len(orders)


        template = loader.get_template("orders/all_orders.html")
        context = {
            "count_orders":count_orders,
            "orders":orders,
        }
        return HttpResponse(template.render(context,request)) 