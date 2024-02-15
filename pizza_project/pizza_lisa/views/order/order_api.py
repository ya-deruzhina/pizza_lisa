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

    # Страница Заказа после оформления
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


    # Формирование Заказа 
    def post(self,request):

        with transaction.atomic():
           # Формирование заказа и запись в БД Orders и Pizza in order
            id_user = request.user.id
            basket = BasketModel.objects.filter(user=id_user)
            catalog = CatalogModel.objects.all()
            price_all = 0
            n=1
            data_pizza = {}

            for pizza in basket:
                if catalog.get(id = pizza.pizza_id).price_disсont !=0:
                    price_one = catalog.get(id = pizza.pizza_id).price_disсont
                else:
                    price_one = catalog.get(id = pizza.pizza_id).price
                    if User.objects.get(id = id_user).discont != 0:
                        price_one = round(price_one * (1-(User.objects.get(id=id_user).discont/100)), 2)
                price_all += price_one * pizza.count
                data_pizza[n] = {'count':pizza.count, 'pizza':pizza.pizza_id,'price_one':price_one}           
                n+=1


            # Получение данных от клиента
            try:
                user = request.user.username
                phone = request.user.phone_number
                comment = request.POST.get('comment')
                address =  request.POST.get('address',"Self-pickup")
                
                data_client = {
                    "user":id_user, 
                    "name":user,
                    "phone":phone,
                    "comment":comment,
                    "address":address,
                    "total_money":price_all
                    }
                
                serializer = OrderSerializer(data=data_client)
                serializer.is_valid(raise_exception=True)
            
            except Exception as exs:
                print ('Warming!!!', exs)   
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render())
            
            else:
                serializer.save()


            # Запись пиццы в PizzaInOrder
                order_number = OrderModel.objects.filter(user=id_user).order_by('-order_time')[0].id
                for a in data_pizza.keys():
                    data = data_pizza[a]
                    # data['order']  = order_number
                    data = {'order':order_number,'count':data['count'], 'pizza':data['pizza'],'price_one':data['price_one']}
                    # import pdb; pdb.set_trace()
                    try:
                        serializer = OrderPizzaSerializer(data=data)
                        serializer.is_valid(raise_exception=True)
                    
                    except Exception as exs:
                        print ('Warming!!!', exs)   
                        template = loader.get_template("main/page_404.html")
                        return HttpResponse(template.render())

                    else:        
                        serializer.save()

             # Удаление из корзины
            basket.delete()

            # Запись скидочной карты при заказе от 50р
            try:
                user = User.objects.get(id = id_user)
                discont = user.discont

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
    
