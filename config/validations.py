from django.core.exceptions import ValidationError
from PIL import Image
from django.utils.translation import gettext_lazy as _
import imghdr


def validate_square_image(image):
    img = Image.open(image)
    if img.width != img.height:
        raise ValidationError("Изображение должно быть квадратным (ширина должна быть равна высоте).")


def validate_horizontal_image(image):
    img = Image.open(image)
    if img.width < img.height:
        raise ValidationError("Изображение должно быть горизонтальным (ширина должна быть больше высоты).")


def validate_png_image(image):
    image_format = imghdr.what(image)
    if image_format != 'png':
        raise ValidationError('Неверный формат изображения. Разрешенный формат "PNG".')

