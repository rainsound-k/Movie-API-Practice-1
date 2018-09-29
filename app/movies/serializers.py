from rest_framework import serializers, exceptions

from .models import Genre, Torrent, Movie

__all__ = (
    'TorrentSerializer',
    'MovieSerializer',
)


class TorrentSerializer(serializers.ModelSerializer):
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
    genres = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Genre.objects.all(), required=True)
    torrents = TorrentSerializer(many=True, required=False)

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

    def create(self, validated_data):
        genres = validated_data.pop('genres', '')
        torrents = validated_data.pop('torrents', '')

        instance = Movie.objects.create(**validated_data)
        if not genres:
            error = {
                'genres': [
                    'This field is required.'
                ]
            }
            raise exceptions.ValidationError(error)

        else:
            genres_list = list(genres)
            for j in range(0, len(genres_list)):
                genre = Genre.objects.get(name=genres_list[j])
                instance.genres.add(genre)

        if torrents:
            torrents_list = list(torrents)
            for k in range(0, len(torrents_list)):
                torrent = Torrent.objects.create(
                    url=torrents_list[k].json().get('url', None),
                    hash=torrents_list[k].json().get('hash', None),
                    quality=torrents_list[k].json().get('quality', None),
                    seeds=torrents_list[k].json().get('seeds', None),
                    peers=torrents_list[k].json().get('peers', None),
                    size=torrents_list[k].json().get('size', None),
                    size_bytes=torrents_list[k].json().get('size_bytes', None),
                    date_uploaded=torrents_list[k].json().get('date_uploaded', None),
                    date_uploaded_unix=torrents_list[k].json().get('date_uploaded_unix', None),
                )
                instance.torrents.add(torrent)
        return instance
