from rest_framework import serializers

from .models import Genre, Torrent, Movie

__all__ = (
    'GenreSerializer',
    'TorrentSerializer',
    'MovieSerializer',
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'name',
        )

    def to_representation(self, obj):
        return obj.name


class TorrentSerializer(serializers.ModelSerializer):
    seeds = serializers.IntegerField(allow_null=True)
    peers = serializers.IntegerField(allow_null=True)
    size_bytes = serializers.IntegerField(allow_null=True)
    date_uploaded_unix = serializers.IntegerField(allow_null=True)

    class Meta:
        model = Torrent
        fields = (
            'url',
            'hash',
            'quality',
            'seeds',
            'peers',
            'size',
            'size_bytes',
            'date_uploaded',
            'date_uploaded_unix',
        )


class MovieSerializer(serializers.ModelSerializer):
    year = serializers.IntegerField()
    runtime = serializers.IntegerField(allow_null=True)
    genres = GenreSerializer(read_only=True, many=True)
    torrents = TorrentSerializer(read_only=True, many=True)
    date_uploaded = serializers.DateTimeField(allow_null=True)
    date_uploaded_unix = serializers.IntegerField(allow_null=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'url',
            'imdb_code',
            'title',
            'title_english',
            'title_long',
            'slug',
            'year',
            'rating',
            'runtime',
            'genres',
            'summary',
            'description_full',
            'synopsis',
            'yt_trailer_code',
            'language',
            'mpa_rating',
            'background_image',
            'background_image_original',
            'small_cover_image',
            'medium_cover_image',
            'large_cover_image',
            'state',
            'torrents',
            'date_uploaded',
            'date_uploaded_unix',
        )