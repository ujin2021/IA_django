from django.urls import path

from . import views
# each app has urls.py -> can manage url easily in mysite urls.py
urlpatterns = [
    path('', views.index, name='index'), # call views.py - def index
]