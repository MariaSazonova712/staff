from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('order', views.order),
    path('add', views.add)
]
