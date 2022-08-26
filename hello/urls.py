from operator import index
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("isaac",views.isaac,name="isaac"),
    path("<str:name>",views.greet,name="greet")
]