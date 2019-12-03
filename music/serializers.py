from rest_framework import serializers

from .models import Artist, ArtistImage, Gender, Album, Track


class ArtistImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArtistImage
        fields = ['url', 'local_image']


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    images = ArtistImageSerializer(many=True, read_only=True)
    serializers.URLField(max_length=200, min_length=None, allow_blank=False)

    class Meta:
        model = Artist
        fields = ['artist_id', 'name', 'images']


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = ['gender_id', 'name']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ['album_id', 'title']


class ArtistAlbumsSerializer(serializers.HyperlinkedModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['artist_id', 'name', 'albums']


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ['track_id', 'name', 'milliseconds']


class AlbumSongsSerializer(serializers.HyperlinkedModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_id', 'title', 'artist_id_id', 'tracks']


class AlbumsFullInformationSerializer(serializers.HyperlinkedModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    artist = ArtistSerializer(source='artist_id', read_only=True)
    longest_track = TrackSerializer(many=False, read_only=True)
    shortest_track = TrackSerializer(many=False, read_only=True)

    class Meta:
        model = Album
        fields = ['album_id', 'title', 'number_of_tracks', 'tracks', 'artist', 'total_length', 'longest_track', 'shortest_track']
