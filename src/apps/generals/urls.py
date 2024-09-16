from django.urls import path
from . import views

app_name = 'generals'

urlpatterns = [
    path('contacts/', views.ContactListAPIView.as_view(), name='contact'),
    path('faq/', views.FAQListAPIView.as_view(), name='faq'),
    path('link_contact/', views.WhatsAppNumberAPIView.as_view(), name='link_contact'),
]
