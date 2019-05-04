from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings
from django.http import HttpResponse

from coingate_api import CoingateAPI, api_error

# Create your views here.

class PaidView(TemplateView):
    template_name = "paid/index.html"    

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            paid_value = float(request.POST.get('value'))
        except ValueError as exception:
            return render(request, self.template_name, {"errors":exception})

        api = CoingateAPI(auth_token=settings.AUTH_TOKEN, environment='sandbox')

        try:
            response = api.create_order(paid_value, "BTC", "USD", success_url="http://127.0.0.1:8000/orders", cancel_url="http://127.0.0.1:8000")
        except api_error.APIError as exception:
            return render(request, self.template_name, {"errors":exception})

        return redirect(response.get("payment_url"))