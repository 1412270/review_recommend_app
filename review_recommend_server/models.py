from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')


class Books(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'books'


class Actors(models.Model):
    person = models.ForeignKey('Persons', models.DO_NOTHING, blank=True, null=True)
    movie = models.ForeignKey('Movies', models.DO_NOTHING, blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actors'


class Collections(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collections'


class Countries(models.Model):
    code = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Directors(models.Model):
    movie = models.ForeignKey('Movies', models.DO_NOTHING, blank=True, null=True)
    director = models.ForeignKey('Persons', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directors'


class Genres(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'


class Keywords(models.Model):
    keyword = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords'


class Languages(models.Model):
    lang_key = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'


class Movies(models.Model):
    title = models.CharField(max_length=1000, blank=True, null=True)
    release_date = models.CharField(max_length=1000, blank=True, null=True)
    budget = models.BigIntegerField(blank=True, null=True)
    revenue = models.BigIntegerField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    original_language = models.ForeignKey(Languages, models.DO_NOTHING, db_column='original_language', blank=True,
                                          null=True)
    belongs_to_collection = models.ForeignKey(Collections, models.DO_NOTHING, db_column='belongs_to_collection',
                                              blank=True, null=True)
    overview = models.CharField(max_length=1000, blank=True, null=True)
    imdb_id = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'


class MoviesGenres(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING, blank=True, null=True)
    genre = models.ForeignKey(Genres, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies_genres'


class MoviesKeywords(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING, blank=True, null=True)
    keyword = models.ForeignKey(Keywords, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies_keywords'


class MoviesProductionCompanies(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING, blank=True, null=True)
    production_company = models.ForeignKey('ProductionCompanies', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies_production_companies'


class Persons(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons'


class ProductionCompanies(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_companies'


class ProductionCountries(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_countries'


class SpokenLanguages(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING, blank=True, null=True)
    language = models.ForeignKey(Languages, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spoken_languages'


class Comments(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    movie = models.ForeignKey('Movies', models.DO_NOTHING, blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    create_time = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'comments'
