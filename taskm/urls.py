from django import views
from django.urls import path
from . import views

app_name="taskm"

urlpatterns = [
    path("",views.index,name="index"),
    path("add",views.add,name="add")
]