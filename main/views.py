from django.shortcuts import render

from main.models import Artist, Song


# Create your views here.
def show(request):
    # artist = Artist.objects.first()
    # print("Artist is", artist)
    # albums = artist.album_set.all()
    # for alb in albums:
    #     print(alb)
    #     songs = alb.song_set.all()
    #     print("Songs under album")
    #     for s in songs:
    #         print(s)

    song = Song.objects.first()
    print(song)
    album = song.album
    print(album)
    artists = album.artists.all()
    print(artists)
    for a in artists:
        print(a.name, a.country, a.dob)


    return render(request, 'index.html')