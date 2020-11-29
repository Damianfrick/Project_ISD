from django.shortcuts import render
from django.http import HttpResponse

def ShowChatHome(request):
    return render(request,"site_one/chat_home.html")

def ShowChatPage(request,room_name,person_name):
    return render(request,"site_one/chat_screen.html", {'room_name':room_name,'person_name':person_name})