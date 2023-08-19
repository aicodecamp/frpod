from easygoogletranslate import EasyGoogleTranslate
 
import pprint
from enum import Enum
import pysbd

def translate(lines : [str], from_lang='fr', to_lang = 'zh-CN')->[str]:
    translated_lines = []
    seg = pysbd.Segmenter(language=from_lang[:2], clean=False)

    #print( f" %%%%%%%%%%%% create translate  : source = {from_lang} target lang ==============={to_lang}")
    translator = EasyGoogleTranslate(    source_language=from_lang,    target_language=to_lang,    timeout=10)
   
    for index, text in enumerate(lines):
        #print("seg=" , len(seg.segment(text)), seg.segment(text))
        translated_sentense = ""
        for sindex, sentense in enumerate( seg.segment(text)):

            translated = translator.translate(sentense)
            translated_sentense += translated 

        translated_lines.append(translated_sentense.strip())

    return translated_lines


if __name__ == '__main__':

    cn = translate(["  C'est clair que ça vaut le détour. Je suis contente de pouvoir partager ça avec toi  ", 'comment vas-tu?'])
    print(cn)
 
