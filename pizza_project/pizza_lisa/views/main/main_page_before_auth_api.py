from django.http import HttpResponse
from django.views import View
from django.template import loader

class FirstPageView(View):
    def get (self, request):
        template = loader.get_template("main/base_page.html")
        return HttpResponse(template.render(request))