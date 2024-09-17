from django.http import JsonResponse
from googletrans import Translator
import json


"""Переводчик для админ панели"""


def translate_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text_to_translate = data.get('text_to_translate', '')
        target_languages = data.get('target_language', ['ru'])

        if text_to_translate:
            translator = Translator()
            translated_texts = [translator.translate(text_to_translate, src='ru', dest=target_lang).text for target_lang
                                in target_languages]
            return JsonResponse({'translated_text': translated_texts})
        else:
            return JsonResponse({'error': 'No text to translate'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)