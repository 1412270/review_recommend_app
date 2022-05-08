from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, CharField, HyperlinkedModelSerializer
from .models import Movies, User, Genres, MoviesGenres


class MoviesSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = ["id", "title", "release_date", "budget", "revenue", "popularity", "runtime", "rating",
                  "original_language", "overview"]


class GenresSerializer(ModelSerializer):
    class Meta:
        model = Genres
        fields = "__all__"


class MoviesGenresSerializer(ModelSerializer):
    class Meta:
        model = MoviesGenres
        fields = ["movie", "genre"]


class MovieDetailSerializer(ModelSerializer):
    genres = SerializerMethodField('set_genres')

    def set_genres(self, movie):
        # get list genre id
        genres_id_list = []
        movies_genres_list = list(MoviesGenres.objects.filter(movie_id=movie.id))
        for item in movies_genres_list:
            genres_id_list.append(MoviesGenresSerializer(item).data['genre'])

        # get list genre name
        genres_name_list = []
        for _id in genres_id_list:
            _genre = Genres.objects.get(pk=_id)
            genre_name = GenresSerializer(_genre).data
            genres_name_list.append(genre_name)
        return genres_name_list

    class Meta:
        model = Movies
        fields = ["id", "title", "release_date", "budget", "revenue", "popularity", "runtime", "rating",
                  "original_language", "overview", "genres"]


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extract_kwargs = {
            'password': {'write_only': 'true'}
        }
