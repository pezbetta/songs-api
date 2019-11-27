from django.db import models


class Artist(models.Model):
    artist_id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=120)


class ArtistImage(models.Model):
    image_id = models.IntegerField(primary_key=True, auto_created=True)
    artist_id = models.ForeignKey(
        'Artist',
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField()


class Album(models.Model):
    album_id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=160)
    artist_id = models.ForeignKey(
        'Artist',
        on_delete=models.CASCADE,
        related_name='albums'
    )

    @property
    def number_of_tracks(self):
        return len(Track.objects.filter(album_id_id=self.pk))

    @property
    def total_length(self):
        tracks = Track.objects.filter(album_id_id=self.pk)
        return sum([track.milliseconds for track in tracks])

    @property
    def longest_track(self):
        return Track.objects.filter(album_id_id=self.pk).order_by('-milliseconds')[0]

    @property
    def shortest_track(self):
        return Track.objects.filter(album_id_id=self.pk).order_by('milliseconds')[0]


class Gender(models.Model):
    gender_id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=120)


class Track(models.Model):
    track_id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    album_id = models.ForeignKey(
        'Album',
        on_delete=models.CASCADE,
        related_name='tracks'
    )
    gender_id = models.ForeignKey(
        'Gender',
        on_delete=models.SET_NULL,
        null=True,
        related_name='tracks'
    )
    milliseconds = models.IntegerField()