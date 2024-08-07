from modeltranslation.translator import register, TranslationOptions
from .models import FAQ, Contact


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address',)



