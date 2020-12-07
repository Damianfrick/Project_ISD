from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'site_home/base.html')

def about(request):
    return render(request, 'site_home/about.html')

def news(request):
    return render(request, 'site_home/news.html')

def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACT US</h1>")
    return render(request, 'site_home/contact.html')