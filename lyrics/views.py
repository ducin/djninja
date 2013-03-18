from django.shortcuts import render, get_object_or_404, redirect
from lyrics.models import Lyric
from django.contrib import auth

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
    lyrics = Lyric.objects.order_by('-created_at')[:5]
    context = { 'songs': lyrics }
    return render(request, 'lyrics/jukebox.html', context)

def lyric(request, lyric_id):
    lyric = get_object_or_404(Lyric, pk=lyric_id)
    context = { 'lyric': lyric }
    return render(request, 'lyrics/song.html', context)

def static_about(request):
    return render(request, 'lyrics/static_about.html', {})

def login(request):
    return render(request, 'lyrics/login.html', {})

def login_process(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('index', {'msg': 'disabled account'})
    else:
        return redirect('index', {'msg': 'invalid login'})
