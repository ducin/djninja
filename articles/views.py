from django.shortcuts import render
from articles.models import Article

def slider(request):
    context = { 'articles': Article.objects.order_by('-created_at')[:5] }
    return render(request, 'articles/slider.html', context)

def archive(request, page=1):
    context = { 'articles': Article.objects.order_by('-created_at')[:5] }
    return render(request, 'articles/archive.html', context)

def detail(request, article_id):
    context = { 'article': get_object_or_404(Article, pk=article_id) }
    return render(request, 'articles/detail.html', context)
