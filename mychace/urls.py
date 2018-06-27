from django.urls import path

from mychace import views

urlpatterns = [
    path('registe', views.registe),
    path('login', views.login)
]
