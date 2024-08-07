from modeltranslation.translator import register, TranslationOptions
from .models import Catalog, Category, Recipe, Price


@register(Catalog)
class CatalogTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Price)
class PriceTranslationOptions(TranslationOptions):
    fields = ('volume',)


@register(Recipe)
class RecipeTranslationOptions(TranslationOptions):
    fields = ('description',)

#
# @register(AditionalStep)
# class AditionalStepsTranslationOptions(TranslationOptions):
#     fields = ('title', 'description')


