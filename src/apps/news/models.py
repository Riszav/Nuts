from django.db import models
from django.utils.translation import gettext_lazy as _
from config.utils import compress
from config import validations


class News(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"))
    image = models.ImageField(_("image"),
                              upload_to='news_images/',
                              **validations.horizontal_image_validator)
    date = models.DateField(_("date"), auto_now_add=True)

    fields_to_translate = ['title', 'description']

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
        db_table = 'news'

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    
class NewsImages(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_images', verbose_name=_('news'))
    image = models.ImageField(_("image"),
                              upload_to='news_gallery/',
                              **validations.horizontal_image_validator)
    
    def __str__(self) -> str:
        return f'{self.pk}'
    
    class Meta:
        verbose_name = _('news image')
        verbose_name_plural = _('news images')
        db_table = 'news_images'

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)