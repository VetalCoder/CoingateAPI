from django.urls import path
from .views import PaidView

urlpatterns = [
    path("", PaidView.as_view()),
    ]