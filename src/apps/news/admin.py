from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from mixins.translations_mixins import TranslatorMediaMixin
from .models import News


@admin.register(News)
class NewsAdmin(TranslatorMediaMixin):
    list_display = ['title', 'description', 'image', 'date']
    list_filter = ['date']
    search_fields = ['title', 'description']

    class Media:
        js = ('translate/autotranslate.js',)
