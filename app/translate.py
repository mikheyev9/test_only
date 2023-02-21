import json
import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if 'TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/get"
    querystring = {"langpair":f"{source_language}|{dest_language}","q":f"{text}","mt":"1","onlyprivate":"0","de":"a@b.c"}
    headers = {
	"X-RapidAPI-Key": "c0b249244amsh6206e610b600a63p1ed913jsn9f78965eea52",
	"X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
    }
    #auth = {'Ocp-Apim-Subscription-Key': app_1.config['MS_TRANSLATOR_KEY']}
    r = requests.request("GET", url, headers=headers, params=querystring)
    #r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
                     #'/Translate?text={}&from={}&to={}'.format(
                        # text, source_language, dest_language),
                     #headers=auth)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))['responseData']['translatedText']