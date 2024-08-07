from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
# class About_us(models.Model):
#     title = models.CharField(max_length=50)
#     text = models.TextField()
#     image1 = models.ImageField(upload_to='about_us', blank=True, null=True)
#     image2 = models.ImageField(upload_to='about_us', blank=True, null=True)
#     #Уточнить по поводу фоток
#
#     def __str__(self):
#         return self.title


class FAQ(models.Model):
    question = models.CharField(_("question"), max_length=200)
    answer = models.TextField(_("answer"))

    fields_to_translate = ['question', 'answer']

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')
        db_table = 'faq'


class Contact(models.Model):
    phone1 = models.CharField(_("phone number 1"), max_length=100)
    phone2 = models.CharField(_("phone number 2"), max_length=100)
    email = models.EmailField(_("email"))
    address = models.CharField(_("address"), max_length=200)
    instagram = models.URLField(_("instagram"))
    facebook = models.URLField(_("facebook"))
    telegram = models.URLField(_("telegram"))
    whatsapp = models.URLField(_("whatsapp"))
    # social_networks = models.ManyToManyField('SocialNetwork', verbose_name=_("social networks"))

    fields_to_translate = ['address']

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        db_table = 'contact'


# SOCIAL_NETWORK_CHOICES = (
#     ('facebook', 'Facebook'),
#     ('instagram', 'Instagram'),
#     ('telegram', 'Telegram'),
#     ('whatsapp', 'Whatsapp')
# )
#
#
# class SocialNetwork(models.Model):
#     name = models.CharField(_("name"), max_length=50, choices=SOCIAL_NETWORK_CHOICES)
#     link = models.URLField(_("link"))
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = _('social network')
#         verbose_name_plural = _('social networks')
#         db_table = 'social_network'
