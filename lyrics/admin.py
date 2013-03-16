from django.contrib import admin
from lyrics.models import Lyric, LyricComment

class LyricInline(admin.StackedInline):
    model = Lyric
    extra = 1

class LyricCommentInline(admin.StackedInline):
    model = LyricComment
    extra = 1

class LyricCommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text_short']

class LyricAdmin(admin.ModelAdmin):
    list_display = ['song', 'lyric_short']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
    search_fields = ['lyric_text']
    fieldsets = [
        (None,      {'fields': ['song', 'created_at']}),
        ('Content', {'fields': ['lyric_text'], 'classes': ['collapse']}),
    ]
    inlines = [LyricCommentInline]
    
admin.site.register(Lyric, LyricAdmin)
admin.site.register(LyricComment)
