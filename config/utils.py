from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    im = Image.open(image)
    im = im.convert('RGB')
    im_io = BytesIO()
    im.save(im_io, 'PNG', quality=50)
    new_image = File(im_io, name=image.name.rsplit('.', 1)[0] + '.png')
    return new_image
    # return image
    # pass