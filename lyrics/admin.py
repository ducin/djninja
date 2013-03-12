from django.contrib import admin
from lyrics.models import Genre, Lyric, LyricComment

class LyricInline(admin.StackedInline):
    model = Lyric
    extra = 1

class LyricCommentInline(admin.StackedInline):
    model = LyricComment
    extra = 1

class LyricCommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text_short']

class LyricAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'lyric_short']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
    search_fields = ['title', 'author']
    fieldsets = [
        (None,      {'fields': ['genre', 'title', 'author', 'album', 'created_at']}),
        ('Content', {'fields': ['lyric_text'], 'classes': ['collapse']}),
    ]
    inlines = [LyricCommentInline]
    

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']
    inlines = [LyricInline]

admin.site.register(Genre, GenreAdmin)
admin.site.register(Lyric, LyricAdmin)
admin.site.register(LyricComment)
