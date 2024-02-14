from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect 
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse

from pizza_lisa.forms import UpdateUserForm 
from pizza_lisa.models import User
from pizza_lisa.serializers import UserUpdateSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.views import APIView

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

# View
class AboutUserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get (self,request):
        user_id = request.user.id
        try:
            user = User.objects.get(id=user_id)
        
        except Exception as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            if user.discont == 0:
                template = loader.get_template("user/user_without_discont.html")
            else:
                template = loader.get_template("user/user.html")
            
            context = {"user" : user}

            return HttpResponse(template.render(context,request))

# Transit Update
class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get (self, request):
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id)

        except Exception as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())

        else:
            template = loader.get_template("user/user_update.html")
            context = {
                "form":UpdateUserForm(),
                "username" : user
            }
            return HttpResponse(template.render(context,request))
    
    
    def post(self,request):    
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            data=request.POST

        except Exception as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
            
        else:
            inv_d = dict(filter(lambda x: x[1] !='', data.items()))
            keys_by_update = list(inv_d.keys())

            if "phone_number" in keys_by_update:
                phone_number = inv_d['phone_number']
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

            if "password" in keys_by_update:
                pas = inv_d ['password']
                passw = make_password(pas)
                inv_d ['password'] = passw

            try:
                instance = User.objects.get(pk=user_id)
                serializer = UserUpdateSerializer (data=inv_d,instance=instance)
                serializer.is_valid(raise_exception=True)
            
            except Exception as exs:
                print ('Warming!!!', exs)   
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render())
            else:
                serializer.save()
                return HttpResponseRedirect ("/pizza/")