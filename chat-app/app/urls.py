from django.urls import path

from app.views import ChatRoomView

urlpatterns = [
    path('chat/', ChatRoomView.as_view(), name='chat_room'),
]