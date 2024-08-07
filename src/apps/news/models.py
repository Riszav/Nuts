from django.db import models
from django.utils.translation import gettext_lazy as _
from utils import compress


class News(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"))
    image = models.ImageField(_("image"), upload_to='news_images')
    date = models.DateField(_("date"), auto_now_add=True)

    fields_to_translate = ['title', 'description']

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
        db_table = 'news'

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)
