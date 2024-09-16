from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .serializers import *
from .models import FAQ, Contact, WhatsAppNumber
from drf_spectacular.utils import extend_schema, extend_schema_view
from decouple import config


@extend_schema(tags=["ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ СПИСКА ЧАСТО ЗАДАВАЕМЫХ ВОПРОСОВ'
    )
)
class FAQListAPIView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


@extend_schema(tags=["КОНТАКТЫ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ КОНТАКТОВ'
    )
)
class ContactListAPIView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.queryset.first()
        serializer = self.serializer_class(queryset).data
        return Response(serializer, 200)
    

@extend_schema(tags=["СВЯЗАТЬСЯ С НАМИ"])
@extend_schema_view(
    get=extend_schema(
        summary='ПОЛУЧЕНИЕ ССЫЛКИ ДЛЯ СВЯЗИ'
    )
)
class WhatsAppNumberAPIView(APIView):
    queryset = WhatsAppNumber.objects.all()
    serializer_class = WhatsAppNumberSerializer
    lookup_field = None

    def get(self, request, *args, **kwargs):
        queryset = self.queryset.first()
        if queryset:
            serializer = self.serializer_class(queryset).data
        else:
            default_number = {'number': config('DEFAULT_WHATSAPP_NUMBER')}
            serializer = self.serializer_class(default_number).data
        return Response(serializer, 200)
    
