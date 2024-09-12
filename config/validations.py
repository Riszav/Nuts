from django.core.exceptions import ValidationError
from PIL import Image
from django.utils.translation import gettext_lazy as _
import imghdr


def validate_square_image(image):
    img = Image.open(image)
    ratio = img.width / img.height
    if ratio < 0.9 or ratio > 1.1:
        raise ValidationError(_("Invalid image. The image must be square."))
        # raise ValidationError("Изображение должно быть квадратным.")

square_image_validator = {
    'help_text': _('The image must be square'),
    'validators': [validate_square_image, ],
}


def validate_horizontal_image(image):
    img = Image.open(image)
    if img.width < img.height:
        raise ValidationError(_("Invalid image. The image must be horizontal (width must be greater than height)."))
        # raise ValidationError("Изображение должно быть горизонтальным (ширина должна быть больше высоты).")

horizontal_image_validator = {
    'help_text': _('The image must be horizontal'),
    'validators': [validate_horizontal_image, ],
}


def validate_png_image(image):
    image_format = imghdr.what(image)
    if image_format != 'png':
        raise ValidationError(_('Invalid image format. Allowed format is "PNG".'))
        # raise ValidationError('Неверный формат изображения. Разрешенный формат "PNG".')

png_image_validator = {
    'help_text': _('The image must be "PNG" format'),
    'validators': [validate_png_image, ],
}

