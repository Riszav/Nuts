from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.apps.news'
    verbose_name = _('News')

    # def ready(self):
    #     import src.apps.news.signals