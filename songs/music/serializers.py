from .models import Artist, Gender, Album, Track
from rest_framework import serializers
from rest_framework.fields import CharField


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['artist_id', 'name']


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = ['gender_id', 'name']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ['album_id', 'title', 'artist_id_id']


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ['track_id', 'name', 'album_id_id', 'gender_id_id', 'milliseconds']


class AlbumSongsSerializer(serializers.HyperlinkedModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_id', 'title', 'artist_id_id', 'tracks']


class AlbumsFullInformationSerializer(serializers.HyperlinkedModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    artist = ArtistSerializer(source='artist_id', read_only=True)
    artist_name = serializers.CharField(source='artist_id.name', read_only=True)

    class Meta:
        model = Album
        fields = ['album_id', 'title', 'tracks', 'artist', 'artist_name']
