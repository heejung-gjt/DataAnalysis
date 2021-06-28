from django.shortcuts import render,redirect
from django.views.generic import View
from scrapping.models import Article, Category, Press
from django.views.generic.detail import DetailView
from django.db.models import Q


class ArticleListView(View):

  def get(self, request, **kwargs):
    context = {}
    articles = Article.objects.filter(category__name='사회').all()
    article_category = Category.objects.filter(name='사회').first()
    article_press = Press.objects.filter(name='인사이트').first()

    context['articles'] = articles
    context['article_category'] = article_category
    context['article_press'] = article_press
    print(articles)
    return render(request, 'news.html',context)


class IndexView(View):
  
  def get(self, request , **kwargs):
    return render(request, 'index.html')


class NewsDetailView(DetailView):

  def get(self, request, **kwargs):
    article = Article.objects.all()
    context={}
    context['articles'] = article
    return render(request, 'all_news.html',context)

  def post(self, request, **kwargs):

    if request.method == 'POST':
      keyword = request.POST['keyword']
      article = Article.objects.filter(Q(title__contains=keyword) | Q(content__contains=keyword)).all().order_by('-date')
      print(article)
      context = {}
      context['articles'] = article
      context['category'] = keyword
      
      return render(request,'news.html', context)
    return redirect('news:list')


class ArticleDetailView(DetailView):

  def get(self, request,**kwargs):
    context = {}

    article = Article.objects.filter(pk=kwargs['pk']).first()
    context['article'] = article
    img = article.img.replace("['",'').replace("']",'').replace("'",'').split(',')
    # print(img)
    cnt = 1
    # for image in img:
    #   context[f'img{cnt}'] = image
    #   cnt+=1
    # print(context['img1'])
    array = []
    for image in img:
      array.append(image)
      context['image'] = array
    return render(request, 'detail.html',context)

  def post(self, request, **kwargs):
    # print('what')
    context = {}

    article = Article.objects.filter(pk=kwargs['pk']).first()
    context['article'] = article
    print(article)
    return render(request, 'detail.html',context)