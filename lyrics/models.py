from django.db import models
from django.db.models.base import ModelBase

class Genre(models.Model):
    """Music genre"""
    class Meta:
        db_table = 'genre'
    name = models.CharField(max_length=64)
    def __unicode__(self):
        return self.name

class Lyric(models.Model):
    """A music lyric"""
    class Meta:
        unique_together = ['title', 'album']
        db_table = 'lyric'
    genre = models.ForeignKey(Genre)
    title = models.CharField(max_length=64)
    lyric_text = models.TextField()
    author = models.CharField(max_length=64)
    album = models.CharField(max_length=64)
    created_at = models.DateTimeField()
    def __unicode__(self):
        return "\"" + self.title + "\" by " + self.author
    def lyric_short(self, length=100):
        return self.lyric_text[:length] + "..."

class LyricComment(models.Model):
    """Comment on a lyric"""
    class Meta:
        db_table = 'lyric_comment'
    lyric = models.ForeignKey(Lyric)
    text = models.TextField()
    author = models.CharField(max_length=64)
    ip = models.CharField(max_length=16)
    created_at = models.DateTimeField()
    def __unicode__(self):
        return "\"" + self.text[:10] + "...\" by " + self.author
    def text_short(self, length=100):
        return self.text[:length] + "..."
    
