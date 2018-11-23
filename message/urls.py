from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),
    path('send/', views.send, name='send'),
    path('chat/<int:receiver_id>', views.chat, name='chat'),
]
