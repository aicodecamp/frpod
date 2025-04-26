import pysubs2
from translate_g import *
from pprint import pprint

# translate_sub: Translates subtitles from one language to one or two target languages and saves the result.
def translate_sub(src_srt: str, dst_srt: str, from_lang:str, to_lang1:str, to_lang2:str):
    subs = pysubs2.load(src_srt)
    pprint(subs)
    lines = [ sub.text for sub in subs]
    translate1_lines = translate(lines, from_lang=from_lang, to_lang=to_lang1 )
    if to_lang2:
        translate2_lines = translate(lines, from_lang=from_lang, to_lang=to_lang2 )


    for index, line in enumerate( subs):
        print(f' translate ----{index}----')

            
        subs[index].text = lines[index] + "\\N" + translate1_lines[index]
        if to_lang2:
            subs[index].text = translate2_lines[index] + "\\N" + subs[index].text 
    

    subs.save(dst_srt)


if __name__ == '__main__':
    srt_srt = 'build/fr-qa/testeur-new.srt'
    dst_srt = 'build/fr-qa/testeur-tr.srt'
    translate_sub(srt_srt, dst_srt, 'fr', 'en', 'zh-CN')