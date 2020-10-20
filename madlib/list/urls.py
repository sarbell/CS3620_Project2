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
    path('soup_form/', views.soup_form, name="soup_form"),
    path('soup_result/', views.soup_result, name="soup_results"),
    path('rage_form/', views.rage_form, name="rage_form"),
    path('rage_result/', views.rage_result, name="rage_results"),
    path('quote_form/', views.quote_form, name="quote_form"),
    path('quote_result/', views.quote_result, name="quote_results"),
    path('poem1_form/', views.poem1_form, name="poem1_form"),
    path('poem1_result/', views.poem1_result, name="poem1_results"),
    path('poem2_form/', views.poem2_form, name="poem2_form"),
    path('poem2_result/', views.poem2_result, name="poem2_results"),
    path('poem3_form/', views.poem3_form, name="poem3_form"),
    path('poem3_result/', views.poem3_result, name="poem3_results"),
    path('trick_form/', views.trick_form, name="trick_form"),
    path('trick_result/', views.trick_result, name="trick_results"),
    path('ghost_form/', views.ghost_form, name="ghost_form"),
    path('ghost_result/', views.ghost_result, name="ghost_results"),
    path('star_form/', views.star_form, name="star_form"),
    path('star_result/', views.star_result, name="star_results"),
    path('farm_form/', views.farm_form, name="farm_form"),
    path('farm_result/', views.farm_result, name="farm_results"),
    path('mice_form/', views.mice_form, name="mice_form"),
    path('mice_result/', views.mice_result, name="mice_results"),
    path('santa_form/', views.santa_form, name="santa_form"),
    path('santa_result/', views.santa_result, name="santa_results"),


]