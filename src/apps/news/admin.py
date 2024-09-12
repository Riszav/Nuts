from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import News, NewsImages
from unfold.admin import ModelAdmin, StackedInline
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class NewsImagesInline(StackedInline):
    model = NewsImages
    fields = ['news', 'image']
    extra = 1
    max_num = 10


@admin.register(News)
class NewsAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['title', 'description', 'news_image', 'date']
    list_display_links = ['title', 'description', 'news_image', 'date']
    list_filter = ['date']
    search_fields = ['title', 'description']
    inlines = (NewsImagesInline, )

    class Media:
        js = ('translate/autotranslate.js',)

    @admin.display(description=_('Image'))
    def news_image(self, img: News):
        return mark_safe(f"<img src='{img.image.url}' width=50 style='border-radius: 5px;'>")

