from django.urls import path
from .views import chat_view

urlpatterns = [
    path('<int:user_id>/', chat_view, name='chat_view'),
]
