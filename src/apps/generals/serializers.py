from rest_framework import serializers
from .models import FAQ, Contact, WhatsAppNumber
from urllib.parse import urlencode
from decouple import config


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['phone1', 'phone2', 'email', 'address', 'instagram', 'facebook', 'telegram', 'whatsapp', 'wildberries', 'ozon']

class WhatsAppNumberSerializer(serializers.ModelSerializer):
    contact_link = serializers.SerializerMethodField()

    class Meta:
        model = WhatsAppNumber
        fields = ['contact_link',]

    def get_contact_link(self, obj):
        base_url = "https://api.whatsapp.com/send"
        number = getattr(obj, 'number', config('DEFAULT_WHATSAPP_NUMBER'))
        params = {'phone': number}
        return f"{base_url}?{urlencode(params)}"
