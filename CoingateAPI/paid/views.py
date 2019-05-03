from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

class PaidView(TemplateView):
    template_name = "paid/index.html"    

    def get(self, request):
        print(settings.AUTH_TOKEN)
        return render(request, self.template_name)

    def post(self, request):
        print(request.POST)
        return HttpResponse(f" In post... {request.POST}")