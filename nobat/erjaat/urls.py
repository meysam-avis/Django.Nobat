
from django.urls import path

from erjaat import views

urlpatterns = [

    path('', views.index, name='index'),

]
