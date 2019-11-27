from .models import Artist, Gender, Album, Track
from rest_framework import viewsets
from .serializers import ArtistSerializer, ArtistAlbumsSerializer, AlbumSerializer, AlbumSongsSerializer, AlbumsFullInformationSerializer
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def list_artist(request):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer(queryset, many=True)
    return Response(serializer_class.data)


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def artist_detail(request, artist_id):
    artist = Artist.objects.get(artist_id=artist_id)
    artist_albums = ArtistAlbumsSerializer(artist, many=False)
    return Response(
        artist_albums.data,
        status.HTTP_200_OK
    )


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def all_album_songs(request):
    albums = Album.objects.all()
    albums_serialized = AlbumSongsSerializer(albums, many=True)
    return Response(
        albums_serialized.data,
        status.HTTP_200_OK
    )


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def album_songs(request, album_id):
    album = Album.objects.get(album_id=album_id)
    album_serialized = AlbumSongsSerializer(album, many=False)
    return Response(
        album_serialized.data,
        status.HTTP_200_OK
    )


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def album_details(request, album_id):
    album = Album.objects.get(album_id=album_id)
    serializer_class = AlbumsFullInformationSerializer(album, many=False)
    return Response(serializer_class.data)
