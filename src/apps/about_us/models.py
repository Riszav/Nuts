from django.db import models
from django.utils.translation import gettext_lazy as _
from config import validations
from django.db.models import UniqueConstraint
from django.core.exceptions import ValidationError
from django_ckeditor_5.fields import CKEditor5Field


class AboutUs(models.Model):
    text = CKEditor5Field(_('text'), max_length=600)
    image = models.ImageField(_('image'), upload_to='about_us_images/', **validations.horizontal_image_validator)

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = _('about us')
        verbose_name_plural = _('about us')
        db_table = 'about_us'


class Banner(models.Model):
    image = models.ImageField(_('image'), upload_to='banner/', blank=True, **validations.horizontal_image_validator)
    video = models.FileField(_('video'), upload_to='banner/', blank=True, **validations.video_validator)
    mobi_image = models.ImageField(_('mobile image'), upload_to='banner/', **validations.square_image_validator)

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banner')
        db_table = 'banner'
        constraints = [
            UniqueConstraint(fields=['image', 'video'], name='unique_banner_image_video')
        ]

    def clean(self):
        if not self.image and not self.video:
            raise ValidationError(_('Either image or video must be provided.'))
        if self.image and self.video:
            raise ValidationError(_('You cannot fill in both fields.'))
