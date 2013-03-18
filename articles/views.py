from django.shortcuts import render
from articles.models import Article

def index(request):
    context = { 'items': Article.objects.order_by('-created_at')[:5] }
    return render(request, 'lyrics/index.html', context)
