import pysubs2
from translate import *


def translate_sub(src_srt: str, dst_srt: str, from_lang:str, to_lang1:str, to_lang2:str):
    subs = pysubs2.load(src_srt)
    lines = [ sub.text for sub in subs]
    translate1_lines = translate(lines, from_lang=from_lang, to_lang=to_lang1 )
    if to_lang2:
        translate2_lines = translate(lines, from_lang=from_lang, to_lang=to_lang2 )


    for index, line in enumerate( subs):
        print( f'------------{index}------------')
        print(line.text)
        subs[index].text = lines[index] + "\\N" + translate1_lines[index]
        if to_lang2:
            subs[index].text = translate2_lines[index] + "\\N" + subs[index].text 
    

    subs.save(dst_srt)


if __name__ == '__main__':
    srt_srt = 'data/subs/sub.srt'
    dst_srt = 'data/subs/sub-tr.srt'
    translate_sub(srt_srt, dst_srt, Languages.fr, Languages.cn, Languages.en)