from django.urls import path
from . import views

urlpatterns = [
    #path('members/', views.members, name='members'),
     path('accounts/', views.members, name='accounts'),
     path('logins/', views.login, name='login'),


]