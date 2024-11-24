from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('organizations/', views.organization_list, name='organization_list'),
    path('users/', views.user_management, name='user_management'),
    path('assign_role/<int:user_id>/', views.assign_role, name='assign_role'),
]
