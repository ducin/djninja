from django.db import models
#from django.db.models.base import ModelBase
from django.core.exceptions import FieldError

class YearField(models.Field):
    def db_type(self, connection):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
            return 'year'
        else:
            raise FieldError

class Genre(models.Model):
    """Music genre"""
    class Meta:
        db_table = 'genre'
    name = models.CharField(max_length=64)
    def __unicode__(self):
        return self.name

class Band(models.Model):
    """Music band"""
    class Meta:
        db_table = 'band'
    name = models.CharField(max_length=64)
    active_since = YearField()
    active_until = YearField(null=True)
    genres = models.ManyToManyField(Genre)
    def __unicode__(self):
        return self.name

class Album(models.Model):
    """Album of a music band"""
    class Meta:
        db_table = 'album'
    band = models.ForeignKey(Band)
    name = models.CharField(max_length=64)
    released_at = models.DateField()
    def __unicode__(self):
        return self.name

class Song(models.Model):
    """Song from a music album"""
    class Meta:
        db_table = 'song'
    band = models.ForeignKey(Band)
    album = models.ForeignKey(Album, null=True)
    title = models.CharField(max_length=64)
    duration = models.IntegerField()
    def __unicode__(self):
        return self.title

