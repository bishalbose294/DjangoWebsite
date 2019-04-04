from django.http import HttpResponse
from .models import Album, Song
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def index(request):
    html_template = loader.get_template("music/musicIndex.html")
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(html_template.render(context, request))


def detail(request, album_id):
    '''
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album doesn't Exist.")
    '''

    album = get_object_or_404(Album, pk=album_id)

    return render(request, 'music/details.html', {'album': album})


def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    try:
        selected_song = album.song_set.get(pk = request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html', {
            'album': album,
            'error_message' : "You have not select a valid song"
        })
    else:
        if selected_song.is_favourite:
            selected_song.is_favourite = False
        else:
            selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})
