from pizza_lisa.models import User, MessagesModel,OrderModel, PizzaInOrder

from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect 

from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.views import APIView

from admin_api.forms import UserForm
from admin_api.serializers import ChangeDiscontSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class AdminAboutUserView(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    # Страница одного пользователя
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)

        except Exception as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("page_404_admin.html")
            return HttpResponse(template.render())

        else:
            user_message = MessagesModel.objects.filter(user_page_id=user_id)
            count_new_message = len(user_message.filter(new = True))
            user_orders = OrderModel.objects.filter(user_id = user_id)
            new_orders = user_orders.filter(status = "NEW").order_by('order_time')
            count_new_orders = len(new_orders)

            template = loader.get_template("about_user/admin_about_user.html")
            context = {
                "user": user,
                "count_new_message":count_new_message,
                "count_new_orders":count_new_orders,
                "new_orders":new_orders,
                "form": UserForm(),
            }
            return HttpResponse(template.render(context,request))  

    # Изменить скидку клиенту
    def post(self, request, user_id):
        try:
            data = request.POST
            instance = User.objects.get(pk=user_id)
            serializer = ChangeDiscontSerializer(data=data,instance=instance)
            serializer.is_valid(raise_exception=True)

        except Exception as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("page_404_admin.html")
            return HttpResponse(template.render())
        else:
            serializer.save()
            return HttpResponseRedirect ("")
 