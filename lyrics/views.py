from django.http import HttpResponse
from django.template import Context, loader

from lyrics.models import Lyric

def index(request):
    template = loader.get_template('lyrics/index.html')
    context = Context({
        'songs': Lyric.objects.order_by('-created_at')[:5]
    })
    return HttpResponse(template.render(context))

def index(request, song_id):
    template = loader.get_template('lyrics/song.html')
    context = Context({
        'song': Lyric.objects.get(id=song_id)
    })
    return HttpResponse(template.render(context))
