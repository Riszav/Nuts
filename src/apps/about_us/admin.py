from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import AboutUs, Banner
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


@admin.register(AboutUs)
class AboutUsAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['id', 'text', 'au_image']
    list_display_links = ['id', 'text', 'au_image']

    class Media:
        js = ('translate/autotranslate.js',)

    @admin.display(description=_('Image'))
    def au_image(self, img: AboutUs):
        return mark_safe(f"<img src='{img.image.url}' width=50 style='border-radius: 5px;'>")

    def save_model(self, request, obj, form, change):
        """
        Разрешаем изменение только первой записи, если она существует.
        """
        if AboutUs.objects.exists() and not change:
            raise ValueError('Можно создать только одну запись.')
        super().save_model(request, obj, form, change)


    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(Banner)
class BannerAdmin(ModelAdmin):

    def save_model(self, request, obj, form, change):
        """
        Разрешаем изменение только первой записи, если она существует.
        """
        if Banner.objects.exists() and not change:
            raise ValueError('Можно создать только одну запись.')
        super().save_model(request, obj, form, change)


    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True