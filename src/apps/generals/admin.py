from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from mixins.translations_mixins import TranslatorMediaMixin, TranslationStackedInlineMixin, TranslationTabularInlineMixin
from .models import Contact, FAQ


@admin.register(FAQ)
class FAQAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('question', 'answer')

    class Media:
        js = ('translate/autotranslate.js',)


@admin.register(Contact)
class ContactAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('phone1', 'phone2', 'email', 'address')

    class Media:
        js = ('translate/autotranslate.js',)

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

