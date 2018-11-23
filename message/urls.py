from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),
    path('send/', views.send, name='send'),
    path('chat/<str:receiver_username>', views.chat, name='chat'),
    path('chatbox/<str:receiver_user>', views.chatbox, name='chatbox'),
]
