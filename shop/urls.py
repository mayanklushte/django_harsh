from django.urls import path
from . import views


urlpatterns = [
    path('index', views.shop_index, name='shop_index')
]
