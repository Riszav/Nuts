from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Contact, FAQ, WhatsAppNumber


@admin.register(FAQ)
class FAQAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('question', 'answer')
    list_display_links = ('question', 'answer')

    class Media:
        js = ('translate/autotranslate.js',)


@admin.register(Contact)
class ContactAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('phone1', 'phone2', 'email', 'address')
    list_display_links = ('phone1', 'phone2', 'email', 'address')

    class Media:
        js = ('translate/autotranslate.js',)

    def save_model(self, request, obj, form, change):
        """
        Разрешаем изменение только первой записи, если она существует.
        """
        if Contact.objects.exists() and not change:
            raise ValueError('Можно создать только одну запись.')
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(WhatsAppNumber)
class WhatsAppAdmin(ModelAdmin):
    list_display = ('number',)
    list_display_links = ('number',)

    def save_model(self, request, obj, form, change):
        """
        Разрешаем изменение только первой записи, если она существует.
        """
        if WhatsAppNumber.objects.exists() and not change:
            raise ValueError('Можно создать только одну запись.')
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True
