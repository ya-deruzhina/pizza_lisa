from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from pizza_lisa.models import MessagesModel
from pizza_lisa.serializers import MessagesSerializer
from pizza_lisa.forms import CreateMessageForm

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class MessageView(APIView):
    # Страница со всеми сообщения + оставить новое
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self,request):
        username = request.user.username
        message = MessagesModel.objects.filter(user_page_id=request.user.id).order_by('date_create')
        template = loader.get_template("messages/messages_main.html")
        context = {
            "messages":message,
            "form":CreateMessageForm(),
            "username":username
        }
        return HttpResponse(template.render(context,request))
    
    def post(self,request):
        message = request.POST.get('message')
        author_message = request.user.username
        try:
            messages = {'message': message, 'user_page': request.user.id, 'author_message':author_message}
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
class MessageDelete (APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request, id):
        try:
            message = MessagesModel.objects.get(id=id)
        
        except Exception  as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            message.delete()
            return HttpResponseRedirect ("/pizza/lisa/message/")
    