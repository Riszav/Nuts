# from urllib.parse import urlencode
# from django.utils.translation import activate, gettext_lazy as _


# class ProductWhatsAppLinkGenerator:

#     @staticmethod
#     def generate_whatsapp_link(obj, admin_number, language):
#         activate(language)

#         base_url = "https://api.whatsapp.com/send"
#         message = _(f"Hello, I want to order {obj.product.name}. Price: {obj.price}. Volume: {obj.volume}")
#         params = {'phone': admin_number, 'text': message}
#         return f"{base_url}?{urlencode(params)}"
