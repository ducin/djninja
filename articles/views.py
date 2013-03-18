from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from articles.models import Article

def slider(request):
    context = { 'articles': Article.objects.order_by('-created_at')[:5] }
    return render(request, 'articles/slider.html', context)

def detail(request, article_id):
    context = { 'article': get_object_or_404(Article, pk=article_id) }
    return render(request, 'articles/detail.html', context)

def archive(request, page="1"):
    articles_list = Article.objects.all().filter(active=True)
    paginator = Paginator(articles_list, 6)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render_to_response('articles/archive.html', {'articles': articles})
