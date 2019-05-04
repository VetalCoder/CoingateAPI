from django.urls import path
from .views import PaidView

app_name = "paid"

urlpatterns = [
    path("", PaidView.as_view(), name="pay"),
    ]