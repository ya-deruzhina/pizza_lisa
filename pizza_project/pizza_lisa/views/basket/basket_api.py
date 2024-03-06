from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

from pizza_lisa.models import BasketModel, User, CatalogModel
from pizza_lisa.serializers import BasketSerializer
from pizza_lisa.forms import CreateOrderForm


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return   # To not perform the csrf check previously happening


class BasketView(APIView):
    # Страница корзины
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self,request, **kwargs):
        id_user = request.user.id
        user_basket = BasketModel.objects.filter(user_id=id_user).order_by('pizza_id')
        basket_with_price = {}
        all_price = 0
        price_without_discont = 0

        for basket in range (0,len(user_basket)):
            baskets ={}
            baskets['pizza'] = user_basket[basket].pizza.name_pizza
            baskets['count'] = user_basket[basket].count
            baskets['one_price_without_discont'] = user_basket[basket].pizza.price
            user_discont = User.objects.get(id = id_user).discont
            
            if user_basket[basket].pizza.price_disсont !=0:
                baskets['price_one'] = user_basket[basket].pizza.price_disсont
            else:
                if user_discont != 0:
                    baskets['price_one'] = round(user_basket[basket].pizza.price * (1-(user_discont/100)), 2)
                else:
                    baskets['price_one'] = user_basket[basket].pizza.price

            baskets['price'] = round((baskets['count'] * baskets['price_one']),2)
            all_price += baskets['price']
            
            baskets ['basket_without_discont'] = baskets['count'] * baskets['one_price_without_discont']
            price_without_discont += baskets ['basket_without_discont']
                        
            baskets['id'] = user_basket[basket].id
            basket_with_price[basket] = baskets
        
        discont = round((price_without_discont - all_price),2)
        price_without_discont = round(price_without_discont,2)
        all_price = round(all_price,2)

        keys = basket_with_price.keys()
        context = {
            "basket_with_price":basket_with_price,
            "form":CreateOrderForm(),
            "keys":keys,
            "all_price": all_price,
            "discont":discont,
            "price_without_discont":price_without_discont,
        }
        if all_price != price_without_discont:
            template = loader.get_template("basket/basket_with_discont.html")
        else:
            template = loader.get_template("basket/basket.html")

        return HttpResponse(template.render(context,request))
    
    def post (self, request, pizza_id):
        user_id = request.user.id
        pizza_for_user = BasketModel.objects.filter(pizza=pizza_id)

        try:
            users_with_pizza = pizza_for_user.get(user=user_id)
        except:
            basket = {'user':user_id,'pizza':pizza_id,'count':1}
            try:
                serializer = BasketSerializer(data=basket)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        
            except Exception as exs:
                print ('Warming!!!', exs)   
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render())
        
        else:
            users_with_pizza.count += 1
            users_with_pizza.save()

        try:
            catalog_amount = CatalogModel.objects.get(id=pizza_id)
            if catalog_amount.amount == 0:
                template = loader.get_template("catalog/error_not_pizza.html")
                return HttpResponse(template.render())
            else:
                catalog_amount.amount -= 1
                catalog_amount.save()

        except Exception as exs:
                print ('Warming!!!', exs)   
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render())

        return HttpResponseRedirect ("/pizza/lisa/basket/") 
    
class BasketDelete(APIView):
    permission_classes = [IsAuthenticated]
    # Удаляет 1 шт из корзины - при 0 шт удаляет запись из БД
    def get (self,request, basket_id):
        try:
            basket = BasketModel.objects.get(id=basket_id)
            
        except Exception  as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            basket.count -=1
            basket.save()

            if basket.count == 0:
                basket.delete()
            
            try:
                catalog_amount = CatalogModel.objects.get(id=basket.pizza_id)
                catalog_amount.amount += 1
                catalog_amount.save()
                
            except Exception as exs:
                    print ('Warming!!!', exs)   
                    template = loader.get_template("main/page_404.html")
                    return HttpResponse(template.render())
    
        return HttpResponseRedirect ("/pizza/lisa/basket/")
    

class BasketAdd(APIView):
    permission_classes = [IsAuthenticated]
    # Добавляет 1 шт в корзину
    def get (self,request, basket_id):
        try:
            basket = BasketModel.objects.get(id=basket_id)

        except Exception  as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            basket.count +=1


        try:
            catalog_amount = CatalogModel.objects.get(id=basket.pizza_id)
            if catalog_amount.amount == 0:
                template = loader.get_template("catalog/error_not_pizza.html")
                return HttpResponse(template.render())
            else:
                catalog_amount.amount -= 1
                catalog_amount.save()
            
        except Exception as exs:
                print ('Warming!!!', exs)   
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render())
        
        basket.save()

        return HttpResponseRedirect ("/pizza/lisa/basket/")
    