from . import views
from django.urls import path

app_name = "list"
urlpatterns = [
    path('', views.home, name="home"),
    path('brick_form/', views.brick_form, name="brick_form"),
    path('brick_result/', views.brick_result, name="brick_results"),
    path('september_form/', views.september_form, name="september_form"),
    path('september_result/', views.september_result, name="september_results"),
    path('rock_form/', views.rock_form, name="rock_form"),
    path('rock_result/', views.rock_result, name="rock_results"),
    path('cookies_form/', views.cookies_form, name="cookies_form"),
    path('cookies_result/', views.cookies_result, name="cookies_results"),



]