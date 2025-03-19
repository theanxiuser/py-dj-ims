from django.shortcuts import render
from django.views import View


class ChatRoomView(View):
    def get(self, request):
        return render(request, 'chat_room.html')