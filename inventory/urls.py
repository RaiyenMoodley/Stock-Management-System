from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.radiator_list, name='radiator_list'),
    path('create/', views.radiator_create, name='radiator_create'),
    path('<int:pk>/edit/', views.radiator_update, name='radiator_update'),
    path('<int:pk>/delete/', views.radiator_delete, name='radiator_delete'),
]

