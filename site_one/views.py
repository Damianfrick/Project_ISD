from django.shortcuts import render
from django.http import HttpResponse

def ShowChatHome(request):
    return render(request,"site_one/chat_home.html")

def ShowChatPage(request,person_name):
    return render(request,"site_one/chat_screen.html", {'person_name':person_name})