from django.urls import path
from . import views

app_name= "app2"

urlpatterns = [
    path("", views.app2_list, name="list")
    #name 중복이면 혼동
]
