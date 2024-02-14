from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.db import transaction

from pizza_lisa.models import User, CatalogModel,BasketModel,OrderModel, PizzaInOrder
from pizza_lisa.serializers import OrderSerializer,OrderPizzaSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.views import APIView

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self,request):
        try: 
            user = User.objects.get(id=request.user.id)
            order_number = OrderModel.objects.filter(user=request.user.id).order_by('-order_time')[0].id
            order_pizza = OrderModel.objects.get(id=order_number)
            pizza_in_order = PizzaInOrder.objects.filter(order=order_number)
        
        except Exception as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())

        else:
            template = loader.get_template("order/order.html")
            context = {
                "order_pizza":order_pizza,
                "pizza":pizza_in_order,
                "user":user,
            }
            return HttpResponse(template.render(context,request))

    # @csrf_exempt
    def post(self,request):

        with transaction.atomic():
            # Получение данных от клиента
            try:
                id_user = request.user.id
                user = request.user.username
                phone = request.user.phone_number
                comment = request.POST.get('comment')
                address =  request.POST.get('address',"Self-pickup")

                data_client = {
                    "user":id_user, 
                    "name":user,
                    "phone":phone,
                    "comment":comment,
                    "address":address
                    }
                
                serializer = OrderSerializer(data=data_client)
                serializer.is_valid(raise_exception=True)
            
            except Exception as exs:
                print ('Warming!!!', exs)   
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render())
            
            else:
                serializer.save()

            # Формирование заказа и запись в БД Orders и Pizza in order
            order_number = OrderModel.objects.filter(user=id_user).order_by('-order_time')[0].id

            basket = BasketModel.objects.filter(user=id_user)
            catalog = CatalogModel.objects.all()
            price_all = 0
            
            for pizza in basket:
                if catalog.get(id = pizza.pizza_id).price_disсont !=0:
                    price_one = catalog.get(id = pizza.pizza_id).price_disсont
                else:
                    price_one = catalog.get(id = pizza.pizza_id).price
                    if User.objects.get(id = id_user).discont != 0:
                        price_one = round(price_one * (1-(User.objects.get(id=id_user).discont/100)), 2)
                data_pizza = {'order':order_number,'count':pizza.count, 'pizza':pizza.pizza_id,'price_one':price_one}

                try:
                    serializer = OrderPizzaSerializer(data=data_pizza)
                    serializer.is_valid(raise_exception=True)
                
                except Exception as exs:
                    print ('Warming!!!', exs)   
                    template = loader.get_template("main/page_404.html")
                    return HttpResponse(template.render())

                else:        
                    serializer.save()
                
                price_all += price_one * pizza.count
            
            # Удаление из корзины
            basket.delete()
            
            # Запись скидочной карты при заказе от 50р
            try:
                discont = User.objects.get(id = id_user).discont

            except Exception as exs:
                    print ('Warming!!!', exs)   
                    template = loader.get_template("main/page_404.html")
                    return HttpResponse(template.render())
            
            else:            
                if price_all > 50 and discont == 0:
                    user = User.objects.get (id = id_user)
                    user.discont = 3      
                    user.save()
            

        return HttpResponseRedirect ("/pizza/lisa/order/")
    
