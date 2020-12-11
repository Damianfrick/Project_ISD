from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key="5fe2cb41f9fb4d36894e6fb826c8228c")
    topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)


    return render(request, 'site_two/base.html', context={"mylist":mylist})



"""def bbc(request):
    newsapi = NewsApiClient(api_key="5fe2cb41f9fb4d36894e6fb826c8228c")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)


    return render(request, 'bbc.html', context={"mylist":mylist})"""