from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('completed/', completed, name='completed'),
    path('active/', active, name='active'),
    path('controller/', controller, name='controller' ),
    path('create-task/', create_task, name='create-task'),
    path('finish-task/', finish_task, name='finish-task')
]