from pizza_lisa.models import User,OrderModel

from django.template import loader
from django.http import HttpResponse 

from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView


class AllOrdersInWorkView(APIView):
    permission_classes = [IsAdminUser]
    # Страница со всеми заказами кроме в архиве + отмененные
    def get(self, request):
        orders = OrderModel.objects.exclude(status='ARCHIVE').exclude(status='CANCELED').order_by('id')
        count_orders = len(orders)

        template = loader.get_template("orders/all_orders_in_work.html")
        context = {
            "count_orders":count_orders,
            "orders":orders,
        }
        return HttpResponse(template.render(context,request)) 