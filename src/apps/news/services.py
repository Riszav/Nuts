class NewsServices:
    """Сервис для работы с изображениями новостей"""

    @staticmethod
    def get_images(obj):
        """Получить список изображений из основной и связанной модели"""
        images = []

        if obj.image:
            images.append(obj.image.url)

        related_images = obj.news_images.all()
        for img in related_images:
            images.append(img.image.url)

        return images