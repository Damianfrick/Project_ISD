"""from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'site_three/base.html')

    """

from django.shortcuts import render
from django.http import HttpResponse

def ShowChatHome(request):
    return render(request,"site_three/chat_home.html")

def ShowChatPage(request,room_name,person_name):
    return render(request,"site_three/chat_screen.html", {'room_name':room_name,'person_name':person_name})