from django.contrib import admin
from django.urls import path
from scrapping.views import ArticleListView, NewsDetailView, ArticleDetailView

app_name = 'news'
urlpatterns = [
    path('detail/', ArticleListView.as_view(), name='index'),
    path('list/', NewsDetailView.as_view(), name='list' ),
    path('detail/<pk>', ArticleDetailView.as_view(), name='detail' ),
]
