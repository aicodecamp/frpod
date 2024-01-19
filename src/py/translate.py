
import ctranslate2
import transformers
import pprint
from enum import Enum
import pysbd

class Languages(str, Enum):
    en = 'eng_Latn'
    fr = 'fra_Latn'
    cn = 'zho_Hans'


def translate(lines : [str], from_lang=Languages.fr, to_lang = Languages.cn)->[str]:

    # src_lang = "eng_Latn"
    # tgt_lang = "fra_Latn"
    # cn_lang = 'zho_Hans'
    # text =  '''
    # Woman: Hi there.
    # Man: Hi. I haven't seen you around here before. Have you been working long?
    # Woman: No, I've only been here a few months. I work in the Human Resources Department.
    # '''
    translated_lines = []
    translator = ctranslate2.Translator("data/models/nllb-200-3.3B", 'cuda')
    #translator = ctranslate2.Translator("nllb-200-600M")
    tokenizer = transformers.AutoTokenizer.from_pretrained("facebook/nllb-200-3.3B", src_lang=from_lang)
    seg = pysbd.Segmenter(language=from_lang[:2], clean=False)
    for index, text in enumerate(lines):

        print("seg=" , len(seg.segment(text)), seg.segment(text))
        translated_sentense = ""
        for sindex, sentense in enumerate( seg.segment(text)):

        

            source = tokenizer.convert_ids_to_tokens(tokenizer.encode(sentense))
            target_prefix = [to_lang]
            results = translator.translate_batch([source], target_prefix=[target_prefix], asynchronous=False)
            #target = results[0].hypotheses[0][1:]
            target = results[0].hypotheses[0]
            results_num = len(results)
            hypotheses_num = len(results[0].hypotheses)
            # print(f' {results_num}', f'{hypotheses_num}')
            # print(f'source = {source}')
            translated  = tokenizer.decode(tokenizer.convert_tokens_to_ids(target))
            translated_sentense += translated[8:] 

        #print(tokenizer.decode(tokenizer.convert_tokens_to_ids(target)))
        #print(translated_text)
        translated_lines.append(translated_sentense.strip())

    return translated_lines


if __name__ == '__main__':

    cn = translate(["  C'est clair que ça vaut le détour. Je suis contente de pouvoir partager ça avec toi  ", 'comment vas-tu?'])
    print(cn)
 