from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import News
from googletrans import Translator


translator = Translator()


@receiver(pre_save, sender=News)
def title_ru(sender, instance, **kwargs):
    if instance.title_ru:
        print('---------------------------------------------------------------------------')
        instance.title_en = translator.translate(instance.title_ru, src='ru', dest='en').text