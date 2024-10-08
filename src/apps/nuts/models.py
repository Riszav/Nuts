from django.db import models
from django.utils.translation import gettext_lazy as _
from config.utils import compress
from config import validations
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(_("name"), max_length=50)

    def __str__(self) -> str:
        return f'{self.name_ru} - {self.name_en}'

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("description"), blank=True, max_length=400)
    hit_of_sales = models.BooleanField(default=False, verbose_name=_("hit of sales"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catalogs', verbose_name=_("category"))
    image = models.ImageField(verbose_name=_("image"),
                              upload_to='catalog_images/',
                              **validations.square_image_validator)

    fields_to_translate = ['name']

    def __str__(self) -> str:
        return f'{self.name_ru} - {self.name_en}'

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        db_table = 'product'

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='catalog_images', verbose_name=_('product'))
    image = models.ImageField(_("image"),
                              upload_to='product_gallery/',
                              **validations.horizontal_image_validator)
    
    def __str__(self) -> str:
        return f'{self.pk}'
    
    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')
        db_table = 'product_images'

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices', verbose_name=_("product"))
    volume = models.CharField(max_length=10, verbose_name=_("volume"))
    price = models.DecimalField(max_digits=8, decimal_places=0)

    def __str__(self) -> str:
        return self.volume

    class Meta:
        verbose_name = _('price')
        verbose_name_plural = _('prices')
        db_table = 'catalog_price'


class Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='recipes', verbose_name=_("product"))
    description = CKEditor5Field(_("description"))
    image = models.ImageField(_("image"),
                              upload_to='recipe_images/',
                              **validations.png_image_validator)
    link = models.URLField(_("link"))

    fields_to_translate = ['description']

    @property
    def product_title(self):
        return self.product.name

    class Meta:
        verbose_name = _('recipe')
        verbose_name_plural = _('recipes')
        db_table = 'recipe'

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)
