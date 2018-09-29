from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Torrent(models.Model):
    url = models.URLField()
    hash = models.CharField(max_length=200, blank=True)
    quality = models.CharField(max_length=50, blank=True)
    seeds = models.PositiveIntegerField(blank=True, null=True)
    peers = models.PositiveIntegerField(blank=True, null=True)
    size = models.CharField(max_length=50, blank=True)
    size_bytes = models.PositiveIntegerField(blank=True)
    date_uploaded = models.DateTimeField(blank=True, null=True)
    date_uploaded_unix = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.url


class Movie(models.Model):
    url = models.URLField()
    imdb_code = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200)
    title_english = models.CharField(max_length=200, blank=True)
    title_long = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=200, blank=True)
    year = models.PositiveIntegerField()
    rating = models.FloatField()
    runtime = models.PositiveIntegerField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    summary = models.CharField(max_length=500, )
    description_full = models.CharField(max_length=500, blank=True)
    synopsis = models.CharField(max_length=500, blank=True)
    yt_trailer_code = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=100, blank=True)
    mpa_rating = models.CharField(max_length=50, blank=True)
    background_image = models.URLField(blank=True)
    background_image_original = models.URLField(blank=True)
    small_cover_image = models.URLField(blank=True)
    medium_cover_image = models.URLField(blank=True)
    large_cover_image = models.URLField(blank=True)
    state = models.CharField(max_length=50, blank=True)
    torrents = models.ManyToManyField(Torrent, blank=True)
    date_uploaded = models.DateTimeField(blank=True, null=True)
    date_uploaded_unix = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
