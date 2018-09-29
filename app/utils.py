import os

import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()
from movies.models import Genre, Torrent, Movie


def get_movie(total_page_num):
    url = 'https://yts.am/api/v2/list_movies.json'
    for page_num in range(1, total_page_num + 1):
        params = {
            'page': page_num,
        }
        response = requests.get(url, params)
        response_dict = response.json()
        movies_list = response_dict['data'].get('movies', '')

        if movies_list:
            for i in range(len(movies_list)):
                movie = Movie.objects.create(
                    url=movies_list[i].get('url', ''),
                    imdb_code=movies_list[i].get('imdb_code', ''),
                    title=movies_list[i].get('title', ''),
                    title_english=movies_list[i].get('title_english', ''),
                    title_long=movies_list[i].get('title_long', ''),
                    slug=movies_list[i].get('slug', ''),
                    year=movies_list[i].get('year', ''),
                    rating=movies_list[i].get('rating', ''),
                    runtime=movies_list[i].get('runtime', ''),
                    summary=movies_list[i].get('summary', ''),
                    description_full=movies_list[i].get('description_full', ''),
                    synopsis=movies_list[i].get('synopsis', ''),
                    yt_trailer_code=movies_list[i].get('yt_trailer_code', ''),
                    language=movies_list[i].get('language', ''),
                    mpa_rating=movies_list[i].get('mpa_rating', ''),
                    background_image=movies_list[i].get('background_image', ''),
                    background_image_original=movies_list[i].get('background_image_original', ''),
                    small_cover_image=movies_list[i].get('small_cover_image', ''),
                    medium_cover_image=movies_list[i].get('medium_cover_image', ''),
                    large_cover_image=movies_list[i].get('large_cover_image', ''),
                    state=movies_list[i].get('state', ''),
                    date_uploaded=movies_list[i].get('date_uploaded', ''),
                    date_uploaded_unix=movies_list[i].get('date_uploaded_unix', ''),
                )
                genres_list = movies_list[i].get('genres', '')
                if genres_list:
                    for j in range(0, len(genres_list)):
                        if Genre.objects.filter(name=genres_list[j]):
                            genre = Genre.objects.get(name=genres_list[j])
                        else:
                            genre = Genre.objects.create(name=genres_list[j])

                        movie.genres.add(genre)

                torrents_list = movies_list[i].get('torrents', '')
                if torrents_list:
                    for k in range(0, len(torrents_list)):
                        torrent = Torrent.objects.create(
                            url=torrents_list[k].get('url', ''),
                            hash=torrents_list[k].get('hash', ''),
                            quality=torrents_list[k].get('quality', ''),
                            seeds=torrents_list[k].get('seeds', ''),
                            peers=torrents_list[k].get('peers', ''),
                            size=torrents_list[k].get('size', ''),
                            size_bytes=torrents_list[k].get('size_bytes', ''),
                            date_uploaded=torrents_list[k].get('date_uploaded', ''),
                            date_uploaded_unix=torrents_list[k].get('date_uploaded_unix', ''),
                        )
                        movie.torrents.add(torrent)


if __name__ == '__main__':
    num = int(input("저장할 페이지 숫자를 입력해주세요(숫자만 가능합니다): "))
    get_movie(num)
