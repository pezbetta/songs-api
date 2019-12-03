from django.core.management.base import BaseCommand

from music.models import ArtistImage


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        ArtistImage.objects.all().delete()
        self.stdout.write(
            self.style.SUCCESS('Successfully deleted all ArtistImage table')
        )
