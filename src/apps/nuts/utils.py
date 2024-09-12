from urllib.parse import urlencode


class ProductWhatsAppLinkGenerator:

    @staticmethod
    def generate_whatsapp_link(obj, admin_number):
        base_url = "https://api.whatsapp.com/send"
        message = f"Здравствуйте, я хочу заказать {obj.product.name}. Цена: {obj.price}. Объем: {obj.volume}"
        params = {'phone': admin_number, 'text': message}
        return f"{base_url}?{urlencode(params)}"
