from django.core.management.base import BaseCommand, CommandError

from music.models import Artist, ArtistImage


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('artist_id', nargs='*', type=int)
        parser.add_argument('--all', action='store_true', help='Download pictures for all artist in DB')

    def handle(self, *args, **options):
        artists = []
        if options['all']:
            artists = Artist.objects.all()
        for artist_id in options['artist_id']:
            try:
                artists.append(Artist.objects.get(pk=artist_id))
            except Artist.DoesNotExist:
                raise CommandError('Artist "%s" does not exist' % artist_id)
        self.fetch_artist(artists)

    def fetch_artist(self, artists):
        for artist in artists:
            artist_image = ArtistImage(artist=artist)

            if artist_image.fetch_image():
                artist_image.save()
                self.stdout.write(
                    self.style.SUCCESS('Successfully fetch image for artist {} > {}'.format(
                        artist.pk, artist_image.local_image
                    ))
                )