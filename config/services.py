class ManyImagesServices:
    """Сервис для работы с изображениями"""

    @staticmethod
    def get_images_list(obj, request, images_list):
        """Получить список изображений из основной и связанной модели"""
        images = []

        if obj.image:
            images.append(request.build_absolute_uri(obj.image.url))

        related_images = images_list.all()
        for img in related_images:
            images.append(request.build_absolute_uri(img.image.url))

        return images