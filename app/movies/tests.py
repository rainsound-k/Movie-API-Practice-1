from django.test import TestCase

from .models import Movie, Genre, Torrent


class MovieTestCase(TestCase):
    def testMovieFields(self):
        genre1 = Genre.objects.create(name='Humman')
        genre2 = Genre.objects.create(name='Funny')
        torrent1 = Torrent.objects.create(
            url='https://yts.am/torrent/download/17DF2AF01AB65BABD71EFA703ASDKWKEWK',
            hash='17DF2AF01AB65BABD71EFA703ASDKWKEWK',
            quality='720P',
            seeds=20,
            peers=11,
            size='1.2 GB',
            size_bytes=1218076626,
            date_uploaded='2018-09-21 05:14:28',
            date_uploaded_unix=1536227390,
        )
        movie = Movie.objects.create(
            title='Test Movie',
            year=2018,
            rating=6.7,
            summary='This is a Test Movie.',
        )
        movie.genres.add(genre1)
        movie.genres.add(genre2)
        movie.torrents.add(torrent1)

        self.assertTrue(movie.rating > 0)
        self.assertTrue(movie.rating < 10)
        self.assertEqual(movie.genres.get(pk=genre1.pk), genre1)
        self.assertEqual(movie.genres.get(pk=genre2.pk), genre2)
        self.assertEqual(movie.torrents.get(pk=torrent1.pk), torrent1)
