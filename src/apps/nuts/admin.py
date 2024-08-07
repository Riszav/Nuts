from django.contrib import admin
from mixins.translations_mixins import TranslatorMediaMixin, TranslationTabularInlineMixin, TranslationMixin
from .models import Category, Catalog, Recipe, Price
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslatorMediaMixin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

    class Media:
        js = ('translate/autotranslate.js',)


class CatalogPriceInline(TranslationTabularInlineMixin):
    model = Price
    fields = ['volume', 'price']
    max_num = 3
    extra = 3

    class Media:
        js = ('translate/autotranslate.js',)


@admin.register(Catalog)
class CatalogAdmin(TranslatorMediaMixin):
    list_display = ['id', 'hit_of_sales', 'name', 'category']
    list_display_links = ['id', 'name']
    inlines = (CatalogPriceInline,)

    class Media:
        js = ('translate/autotranslate.js',)


# class AditionalStepsInline(TranslationTabularInlineMixin):
#     model = AditionalStep
#     fields = ['title', 'description']
#     extra = 0
#
#     class Media:
#         js = ('translate/autotranslate.js',)


@admin.register(Recipe)
class RecipeAdmin(TranslatorMediaMixin):
    list_display = ['id', 'catalog']
    list_display_links = ['id', 'catalog']
    
    class Media:
        js = ('translate/autotranslate.js',)
