from modeltranslation.translator import register, TranslationOptions
from .models import Product, Category, Recipe, Price


@register(Product)
class ProductTranslationOptions(TranslationOptions):
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


