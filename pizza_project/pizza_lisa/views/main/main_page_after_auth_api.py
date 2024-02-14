from django.http import HttpResponse
from django.template import loader

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from pizza_lisa.models import User

class FirstPageAfterAuthView(APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request):
        try:
            first_name = User.objects.get(id=request.user.id).first_name
            
        except Exception as exs:
                print ('Warming!!!', exs)
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render()) 
        else:
            template = loader.get_template("main/base_page_after_auth.html")
            context = {
                "first_name":first_name
            }
            return HttpResponse(template.render(context,request))