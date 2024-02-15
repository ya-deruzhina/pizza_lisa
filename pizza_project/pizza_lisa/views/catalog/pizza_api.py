from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from pizza_lisa.models import CatalogModel, ReviewModel
from pizza_lisa.serializers import ReviewSerializer
from pizza_lisa.forms import ReviewForm

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return   # To not perform the csrf check previously happening


# Страница Одной Пицы  
class PizzaView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get (self,request,pizza_id):
        try:
            pizza = CatalogModel.objects.get(id=pizza_id)
            reviews = ReviewModel.objects.filter(pizza=pizza_id).order_by('time')

        except Exception as exs:
                print ('Warming!!!', exs)
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render()) 
        else:     
            if pizza.price_disсont == 0:
                price = pizza.price
                discont = "Not Sale"
            else:
                price = pizza.price_disсont
                discont = "Sale"
        
        template = loader.get_template("catalog/pizza_review.html")
        context = {
                "pizza" : pizza,
                "form":ReviewForm(),
                "reviews":reviews,
                "price":price,
                "discont":discont,
            }

        return HttpResponse(template.render(context,request))

    # Оставить Отзыв о Пицце
    def post(self,request, pizza_id):
        try:
            data = {"user":request.user.id, "pizza":pizza_id,"review":(request.POST.get('review'))}
            serializer = ReviewSerializer(data=data)
            serializer.is_valid(raise_exception=True)
       
        except Exception as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            serializer.save()
            return HttpResponseRedirect ("")


