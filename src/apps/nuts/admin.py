from django.contrib import admin
from mixins.translations_mixins import TranslatorMediaMixin, TranslationTabularInlineMixin, TranslationMixin
from .models import Category, Product, Recipe, Price
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslatorMediaMixin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ("category", "title")
    class Media:
        js = ('translate/autotranslate.js',)


class ProductPriceInline(TranslationTabularInlineMixin):
    model = Price
    fields = ['volume', 'price']
    max_num = 3
    extra = 3

    class Media:
        js = ('translate/autotranslate.js',)


@admin.register(Product)
class ProductAdmin(TranslatorMediaMixin):
    list_display = ['id', 'hit_of_sales', 'name', 'category']
    list_display_links = ['id', 'name']
    inlines = (ProductPriceInline,)
    autocomplete_fields = ("category", )

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
    list_display = ['id', 'product']
    list_display_links = ['id', 'product']
    
    class Media:
        js = ('translate/autotranslate.js',)
