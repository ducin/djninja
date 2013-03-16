from django.contrib import admin
from bands.models import Genre, Band, Album, Song

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']

admin.site.register(Genre)
admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Song)
