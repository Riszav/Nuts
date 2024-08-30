from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from mixins.translations_mixins import TranslatorMediaMixin
from .models import News
from unfold.admin import ModelAdmin


@admin.register(News)
class NewsAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['title', 'description', 'image', 'date']
    list_filter = ['date']
    search_fields = ['title', 'description']

    class Media:
        js = ('translate/autotranslate.js',)
