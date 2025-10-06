from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details,name='details'),
     #path('accounts/', views.members, name='accounts'),
     path('logins/', views.login, name='login'),


]