from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key="5fe2cb41f9fb4d36894e6fb826c8228c")
    topheadlines = newsapi.get_top_headlines(sources='the-wall-street-journal')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])


    mylist = zip(news, desc, img, url)


    return render(request, 'site_two/base.html', context={"mylist":mylist})



def bbc(request):
    newsapi = NewsApiClient(api_key="5fe2cb41f9fb4d36894e6fb826c8228c")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])


    mylist = zip(news, desc, img, url)


    return render(request, 'site_two/bbc.html', context={"mylist":mylist})

def google(request):
    newsapi = NewsApiClient(api_key="5fe2cb41f9fb4d36894e6fb826c8228c")
    topheadlines = newsapi.get_top_headlines(sources='google-news')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])


    mylist = zip(news, desc, img, url)


    return render(request, 'site_two/google.html', context={"mylist":mylist})

def cnn(request):
    newsapi = NewsApiClient(api_key="5fe2cb41f9fb4d36894e6fb826c8228c")
    topheadlines = newsapi.get_top_headlines(sources='cnn')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])


    mylist = zip(news, desc, img, url)


    return render(request, 'site_two/cnn.html', context={"mylist":mylist})