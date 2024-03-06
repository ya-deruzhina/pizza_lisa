from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.views import View
from django.http import JsonResponse

from pizza_lisa.forms import RegisterForm 
from pizza_lisa.serializers import UserSerializer
from pizza_lisa.models import User


class UserRegistrationView(View):
    def get (self, request):
        template = loader.get_template("user/registrate.html")
        context = {
            "form":RegisterForm()
        }
        return HttpResponse(template.render(context,request))

    def post(self,request):
        phone_number = request.POST.get('phone_number')
        # Мы проверяем на повторение номера, но при сохранении + убирается автоматически
        if phone_number[0] == '+':
            phone_number = phone_number[1:]
        if len (phone_number) != 12:
            return JsonResponse ({'Warning':'Mistake: Not Correct Number. Please, Check'}) 
        if int(phone_number[0:3]) != 375:
            return JsonResponse ({'Warning':"Mistake: Not Start 375"})    
        if int(phone_number [3:5]) not in [29,33,44,25]:
            return JsonResponse ({'Warning':"Mistake: Not Code 29,33,44,25"})
        if 1000000 > int(phone_number [5:]):
            return JsonResponse ({'Warning':"Mistake: Not Real Number"})     
        if len(User.objects.filter(phone_number=phone_number)) != 0:
            return JsonResponse ({'Warning':"This Phone Number Used"})
        else:
            try:
                serializer = UserSerializer(data=request.POST)
                serializer.is_valid(raise_exception=True)

            except Exception as exs:
                print ('Warming!!!', exs)   
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render())

            else:
                serializer.save()
                user = User.objects.get (username = request.POST.get('username'))
                pas = request.POST.get('password')
                passw = make_password(pas)
                user.password = passw
                user.save() 
                return HttpResponseRedirect ("/pizza/")