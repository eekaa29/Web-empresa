from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name= "home"),
    path('about/', views.about_us, name= "about"),
    path('store/', views.visit_us, name= "store"),
    path('contact/', views.contact, name= "contact"),
    path('sample/', views.sample, name= "sample"),
]