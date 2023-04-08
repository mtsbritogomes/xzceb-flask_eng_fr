import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(API_KEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

def english_to_french(english_text):

    translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        source='en',
        target='fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Traduz um texto em francês para inglês.

    Args:
        french_text: O texto em francês a ser traduzido.

    Returns:
        O texto traduzido em inglês.
    """
    translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        source='fr',
        target='en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
