from django.urls import path
from .views import home, user_list

urlpatterns = [
    path('', home, name='home'),
    path('users/', user_list, name='user_list'),
]
