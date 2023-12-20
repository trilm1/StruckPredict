from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home),
    path('workspace/', views.get_workSpace),
    path('action/', views.get_action),
    path('anotherAction/', views.get_anotherAction),
    path('contact/', views.get_contact),
    path('blog/', views.get_blog),
    path('login/', views.go_login),
    path('predict/', views.predict, name='predict'),
]