"""
Module for online translate posts
"""
import json
import requests
from flask_babel import _
from app import current_app


def translate(text, source_language, dest_langauge):
    """
    Translate text from original lang to customer lang

    curl "https://api.nlpcloud.io/v1/nllb-200-3-3b/translation" \
    -H "Authorization: Token <token>" \
    -H "Content-Type: application/json" \
    -X POST -d '{
        "text":"John Doe has been working for Microsoft in Seattle since 1999.",
        "source":"en",
        "target":"fr"
    }'
    """
    if source_language == 'en':
        source_language = 'eng_Latn'
    if dest_langauge == 'ru':
        dest_langauge = 'rus_Cyrl'
    if 'NLP_TRANSLATOR_KEY' not in app.config or \
            not app.config['NLP_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured')
    
    auth = {'Authorization': 'Token ' + app.config['NLP_TRANSLATOR_KEY'], \
            'Content-Type': 'application/json',}
    r = requests.post(
        'https://api.nlpcloud.io/v1/nllb-200-3-3b/translation',
        headers=auth,
        json={'text': text,
                'source':source_language,
                'target':dest_langauge})
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return r.json()['translation_text']
