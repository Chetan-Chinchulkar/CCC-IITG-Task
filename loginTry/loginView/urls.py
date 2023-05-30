from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('user_list/', user_list, name='user_list'),
]
