from rest_framework import serializers
from .models import FAQ, Contact


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['phone1', 'phone2', 'email', 'address', 'instagram', 'facebook', 'telegram', 'whatsapp']
