from django.db import models
from django.utils.translation import gettext_lazy as _
from mixins.translations_mixins import TranslationMixin
from django_ckeditor_5.fields import CKEditor5Field
from utils import compress


class Category(models.Model):
    name = models.CharField(_("name"), max_length=20)

    def __str__(self):
        return f'{self.name_ru} - {self.name_en}'

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(_("name"), max_length=100)
    description = models.TextField(_("description"), blank=True)
    hit_of_sales = models.BooleanField(default=False, verbose_name=_("hit of sales"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catalogs', verbose_name=_("category"))
    image = models.ImageField(_("image"), upload_to='catalog_images', help_text='Разрешенный формат изображения img, jpg, jpeg, phg.')

    fields_to_translate = ['name']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        db_table = 'product'

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices', verbose_name=_("product"))
    volume = models.CharField(max_length=25, verbose_name=_("volume"))
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _('price')
        verbose_name_plural = _('prices')
        db_table = 'catalog_price'


class Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='recipes', verbose_name=_("product"))
    description = models.TextField(_("description"), blank=True)
    image = models.ImageField(_("image"), upload_to='recipe_images')
    link = models.URLField(_("link"))

    fields_to_translate = ['description']

    class Meta:
        verbose_name = _('recipe')
        verbose_name_plural = _('recipes')
        db_table = 'recipe'

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

# class Recipe(models.Model):
#     title = models.CharField(_("title"), max_length=100)
#     ingredients = CKEditor5Field(_("ingredients"), config_name='extends')
#     cooking_method = CKEditor5Field(_("cooking method"), config_name='extends')
#     # add_step = models.ManyToManyField('AditionalSteps', verbose_name=_("additional steps"), blank=True)
#
#     class Meta:
#         verbose_name = _('recipe')
#         verbose_name_plural = _('recipes')
#         db_table = 'recipe'

#
# class AditionalStep(models.Model):
#     title = models.CharField(_("title"), max_length=100)
#     description = CKEditor5Field(_("step"), config_name='extends')
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='addition_steps', verbose_name=_("recipe"))
#
#     class Meta:
#         verbose_name = _('additional step')
#         verbose_name_plural = _('additional steps')
#         db_table = 'additional_step'
