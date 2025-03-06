from django.urls import path
from . import views
urlpatterns = [
    path("passenger/", views.passenger_list),
    path("passenger/<str:pk>",views.passenger_detail),
]
