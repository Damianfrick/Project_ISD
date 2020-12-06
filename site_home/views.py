from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'site_home/base.html')

def about(request):
    return render(request, 'site_home/about.html')

def news(request):
    return render(request, 'site_home/news.html')

def contact(request):
    return render(request, 'site_home/contact.html')