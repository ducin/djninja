from django.http import HttpResponse

from lyrics.models import Lyric

def index(request):
    latest_songs = Lyric.objects.order_by('-created_at')[:5]
    output = ", ".join([s.title for s in latest_songs])
    return HttpResponse(output)
