from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'artist', views.ArtistViewSet)
# router.register(r'gender', views.GenderViewSet)
# router.register(r'album', views.AlbumViewSet)
# router.register(r'track', views.TrackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('artist/', views.list_artist, name='artist'),
    path('artist/<int:artist_id>', views.artist_detail, name='artist_detail'),
    path('album/<int:album_id>', views.album_songs, name='album_detail'),
    path('album/', views.all_album_songs, name='list_albums'),
    path('album_songs/<int:album_id>', views.album_details, name='album_songs')
]
