from django.urls import path
from .views import OrdersView, OrdersDetailView

app_name = "orders_list"

urlpatterns = [
    path("", OrdersView.as_view(), name="orders"),
    path('/<int:order_id>/', OrdersDetailView.as_view(), name='detail'),
    ]
