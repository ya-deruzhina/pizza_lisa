from pizza_lisa.models import User, MessagesModel,OrderModel, PizzaInOrder

from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect 
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse

from admin_api.forms import ChangeStatusOrderForm,UserForm
from pizza_lisa.models import User
from admin_api.serializers import ChangeStatusSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.views import APIView

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class OneOrderPageView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request, order_id):
        user_order = OrderModel.objects.get(id=order_id)
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

    def post(self, request, order_id):
        try:
            data = request.POST
            instance = OrderModel.objects.get(pk=order_id)
            # import pdb; pdb.set_trace()
            serializer = ChangeStatusSerializer (data=data,instance=instance)
            serializer.is_valid(raise_exception=True)

        except Exception as exs:
            # import pdb; pdb.set_trace()
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        else:
            serializer.save()
            return HttpResponseRedirect ("")
