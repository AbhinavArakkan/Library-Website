from django.urls import path
from .views import home, history, news, gallery, news_detail

urlpatterns = [
    path('', home, name='home'),
    path('history/', history, name='history'),
    path('news/', news, name='news'),
    path('gallery/', gallery, name='images'),
    path('news/<int:news_id>/', news_detail, name='news_detail'), 
]