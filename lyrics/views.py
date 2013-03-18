from django.shortcuts import render, get_object_or_404, redirect
from lyrics.models import Lyric
from django.contrib import auth

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
