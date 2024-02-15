from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from pizza_lisa.models import MessagesModel
from pizza_lisa.serializers import MessagesSerializer
from pizza_lisa.forms import CreateMessageForm

from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class MessageAdminView(APIView):
    # Страница со всеми сообщения + оставить новое
    permission_classes = [IsAdminUser]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self,request,user_id):
        message = MessagesModel.objects.filter(user_page_id=user_id).order_by('date_create')
        template = loader.get_template("about_user/messages_main.html")
        context = {
            "messages":message,
            "form":CreateMessageForm(),
            "user_id":user_id
        }
        return HttpResponse(template.render(context,request))
    
    def post(self,request,user_id):
        message = request.POST.get('message')
        author_message = 'admin'
        try:
            messages = {'message': message, 'user_page': user_id, 'author_message':author_message, "new":False}
            serializer = MessagesSerializer(data=messages)
            serializer.is_valid(raise_exception=True)
       
        except Exception as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            serializer.save()
            return HttpResponseRedirect ("")

# Delete message
class MessageAdminDelete (APIView):
    permission_classes = [IsAdminUser]
    def get (self, request, user_id,_id):
        try:
            message = MessagesModel.objects.get(id=_id)
        
        except Exception  as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            message.delete()
            return HttpResponseRedirect (f"/main/user/message/{user_id}")

# Меняет статус на Прочтено        
class MessageAdminRead (APIView):
    permission_classes = [IsAdminUser]
    def get (self, request, user_id,_id):
        try:
            message = MessagesModel.objects.get(id=_id)
        
        except Exception  as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            message.new = False
            message.save()
            return HttpResponseRedirect (f"/main/user/message/{user_id}")
    