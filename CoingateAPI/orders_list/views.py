from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404

from api import CoingateAPI, api_error

# Create your views here.

class OrdersView(TemplateView):
    template_name = "orders_list/index.html"    

    def get(self, request):
        page = int(request.GET.get("page", 1))
        api = CoingateAPI(auth_token=settings.AUTH_TOKEN, environment='sandbox')
        response = api.orders(per_page=5, page=page)

        context = {
            "orders" : response.get("orders"), 
            "pages": response.get("total_pages"), 
            "selected_page" : page
            }

        return render(request, self.template_name, context)


class OrdersDetailView(TemplateView):
    template_name = "orders_list/detail.html"    

    def get(self, request, order_id):

        api = CoingateAPI(auth_token=settings.AUTH_TOKEN, environment='sandbox')

        try:
            response = api.get_order(order_id)
        except api_error.APIError as exception:
            raise Http404(f"Order with id '{order_id}' does not exist")

        context = {
            "order" : response,
            }

        return render(request, self.template_name, context)