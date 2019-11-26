from django.urls import path

from . import views


urlpatterns = [
    path('artist', views.list_artist, name='artist'),
    path('artist/<int:artist_id>', views.artist_detail, name='artist_detail'),
    path('album/<int:album_id>', views.album_songs, name='album_detail'),
    path('album', views.all_album_songs, name='list_albums'),
    path('album/<int:album_id>/detail', views.album_details, name='album_songs')
]
