import os.path

import feedparser
import unicodedata

import json
import re
import requests
from pprint import pprint


from easygoogletranslate import EasyGoogleTranslate

import pprint
from enum import Enum





def strip_accents( text: str)->str:
    return str(unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8'))

def replace_nonalphanumeric( text: str)->str:
    return re.sub('[^0-9a-zA-z]', '-', text)




def down_feed( feed :str, limit =0, download_mp3=True, download_summary=True , translator = None):
    f = feedparser.parse( feed)

    first = f.entries[0]

    #print(json.dumps(f.entries[0], ensure_ascii=True))
    #pprint(first)
    

    folder_name = replace_nonalphanumeric(f.feed.title)
    # folder = f'build/{folder_name}'
    folder_path = os.path.join ( os.path.dirname ( os.path.dirname(os.path.realpath(__file__))), 'build' ,  folder_name)
    

    # create dir
    titleText = {}
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)

    for index, e in enumerate( f.entries):
        if limit >0 and index >= limit:
            break
        #e = f.entries[0]
        #print(e)

        summary = e.summary [:e.summary.rfind('Learn more about')]

        tr_seperator = 'Traduction:'
        fr_end = summary.find(tr_seperator)
        en_start = fr_end + len(tr_seperator)

        summary_fr = summary[:fr_end].strip()
        summary_en = summary[en_start :].strip()
        year, month,day = e.published_parsed[0:3]
        date = str(year) + str(month).zfill(2) + str(day).zfill(2)


        #"type":"audio/mpeg"

        title = date +"-" + e.title
        name = replace_nonalphanumeric(title)




        txt_path = os.path.join(  folder_path , name+".txt")
        mp3_path = os.path.join(  os.path.dirname(os.path.realpath(__file__)), folder_path, name+".mp3")
        #if not os.path.isfile( txt_path) :

        print( f'{name}')

        
        if  download_mp3 and (not os.path.isfile( mp3_path)):
            mp3_link = next((link for link in e.links if link['type'] == 'audio/mpeg'), None )
            mp3_url = mp3_link['href']
            print(f'{mp3_url}')
        

            resp = requests.get(mp3_url)
            mp3_path  = os.path.join(  os.path.dirname(os.path.realpath(__file__)), folder_path, name+".mp3")
            if not os.path.isfile(mp3_path):
                with open( mp3_path , 'wb') as mp3_file:
                    mp3_file.write(resp.content)

        if download_summary and (not os.path.isfile( txt_path)):

            #mp3_url = e.links[0].href
            # find link

            # print(f'en={summary_en}')
            # print(f'fr={summary_fr}')
                    # translate
            summary_zh = translator.translate(summary_fr)
            # print(f'zh={summary_zh}')
            titleText[title] = summary
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.writelines( [ title+"\n", summary_fr+"\n", summary_en+"\n", summary_zh+"\n" ])



            #print( "titles = ", titleText)
            with open(os.path.join (  folder_path ,  "combined_text.csv"), 'a', encoding='utf-8') as combined_file:
                # for title in sorted( titleText.keys() ):
                #     print(title)
                combined_file.writelines( [ f"{title}\t{summary_en}\t{summary_fr}\t{summary_zh}\n"])




if __name__ == '__main__':
    feed_reallife_french = 'https://feeds.megaphone.fm/FODL3433265973'
    feed_french_story = 'https://anchor.fm/s/2960b598/podcast/rss'
    feed_louis ='https://feeds.megaphone.fm/FODL5989341949'

    translator = EasyGoogleTranslate(    source_language='fr',    target_language='zh-CN',    timeout=10)

    down_feed(feed_louis, limit=0,  download_mp3=False,  translator=translator)

