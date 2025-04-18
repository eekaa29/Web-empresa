from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name= "home"),
    path('about/', views.about_us, name= "about"),
    path('store/', views.visit_us, name= "store"),
]