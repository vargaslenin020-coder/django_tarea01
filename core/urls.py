from django.urls import path
from . import views

urlpatterns = [  
    path('hello/', views.hello_world_view, name='hello_world'),
    path('nombre/', views.my_name_view, name='my_name'),
]