from django.db import models

class Article(models.Model):
    """News article, displayed on homepage to attract users"""
    class Meta:
        db_table = 'article'
    title = models.CharField(max_length=64)
    headline = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to = 'articles/', null=True, blank=True)
    active = models.BooleanField()
    created_at = models.DateTimeField()
    def __unicode__(self):
        return self.title
