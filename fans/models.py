from django.db import models

class User(models.Model):
    """Music fan, registered in the system"""
    class Meta:
        db_table = 'user'
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    nick = models.CharField(max_length=64)
    avatar = models.FileField(upload_to='avatar')
    registered_at = models.DateTimeField()
    def __unicode__(self):
        return self.nick + '(' + self.firstname + ' ' + self.lastname + ')'