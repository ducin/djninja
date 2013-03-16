from django.shortcuts import render, get_object_or_404
from lyrics.models import Lyric

def index(request):
    return render(request, 'lyrics/index.html', {})

def jukebox(request):
    songs = Lyric.objects.order_by('-created_at')[:5]
    context = { 'songs': songs }
    return render(request, 'lyrics/jukebox.html', context)

def song(request, song_id):
    song = get_object_or_404(Lyric, pk=song_id)
    context = { 'song': song }
    return render(request, 'lyrics/song.html', context)

def static_about(request):
    return render(request, 'lyrics/static_about.html', {})
