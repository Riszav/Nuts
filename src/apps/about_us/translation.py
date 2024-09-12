from modeltranslation.translator import register, TranslationOptions
from .models import AboutUs


@register(AboutUs)
class NewsTranslationOptions(TranslationOptions):
    fields = ('text',)


