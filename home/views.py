from django.shortcuts import render, get_object_or_404
from .models import Member, Image, NewsItem  

def home(request):
    members = Member.objects.all()
    return render(request, 'home/home.html', {'members': members})

def news(request):
    news_list = NewsItem.objects.all().order_by('-uploaded_date')
    return render(request, 'home/news.html', {'news_list': news_list})

def gallery(request):
    imgs = Image.objects.all()  # Changed from images.objects
    return render(request, 'home/images.html', {'imgs': imgs})

def history(request):
    return render(request, 'home/history.html')

def news_detail(request, news_id):
    news_item = get_object_or_404(NewsItem, pk=news_id)
    return render(request, 'home/news_detail.html', {'news_item': news_item})