from django.db import models
from bands.models import Genre, Song

class Lyric(models.Model):
    """A music lyric"""
    class Meta:
        db_table = 'lyric'
    song = models.ForeignKey(Song,unique=True)
    lyric_text = models.TextField()
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
    ip = models.IPAddressField()
    created_at = models.DateTimeField()
    def __unicode__(self):
        return "\"" + self.text[:10] + "...\" by " + self.author
    def text_short(self, length=100):
        return self.text[:length] + "..."
    
