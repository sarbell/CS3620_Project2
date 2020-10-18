from . import views
from django.urls import path

app_name = "list"
urlpatterns = [
    path('', views.home, name="home"),
    path('start/<int:id>', views.start, name="start"),
    path('show/<int:id>', views.show, name="show"),

    # path('update/<int:id>', views.update_item, name="update_item"),

]