from django.shortcuts import render, get_object_or_404
from lyrics.models import Lyric

def index(request):
    context = { 'items': [
        {
            'image': 'examples/slide-01.jpg',
            'headline': 'Example headline.',
            'lead': 'Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.',
            'button': 'Sign up today',
        },
        {
            'image': 'examples/slide-02.jpg',
            'headline': 'Another example headline.',
            'lead': 'Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit. Cras justo odio, dapibus ac facilisis in, egestas eget quam.',
            'button': 'Learn more',
        },
        {
            'image': 'examples/slide-03.jpg',
            'headline': 'One more for good measure.',
            'lead': 'Nullam id dolor id nibh ultricies vehicula ut id elit. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus.',
            'button': 'Browse gallery',
        },
    ]}
    return render(request, 'lyrics/index.html', context)

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
