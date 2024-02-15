from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from pizza_lisa.models import OrderModel

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Status NEW -> CANCELED
class CancelOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request, order_id):
        try:
            order = OrderModel.objects.get(id = order_id)
        
        except Exception  as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            if order.status == "NEW":
                order.status = "CANCELED"
                order.save()
            else:
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render()) 

            return HttpResponseRedirect ("/pizza/lisa/")