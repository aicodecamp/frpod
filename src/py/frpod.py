import os.path

import feedparser
import unicodedata

import json
import re
import requests

def strip_accents( text: str)->str:
    return str(unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8'))

def replace_nonalphanumeric( text: str)->str:
    return re.sub('[^0-9a-zA-z]', '-', text)

feed_reallife_french = 'https://feeds.megaphone.fm/FODL3433265973'

def down_feed( feed :str):
    f = feedparser.parse( feed)

    folder = replace_nonalphanumeric(f.feed.title)
    # print(json.dumps(f.entries[0]))
    # create dir
    titleText = {}
    if not os.path.isdir(folder):
        os.mkdir(folder)

    for index, e in enumerate( f.entries):
    #e = f.entries[0]
        print(e)

        summary = e.summary [:e.summary.rfind('Learn more about')]
        year, month,day = e.published_parsed[0:3]
        date = str(year) + str(month).zfill(2) + str(day).zfill(2)
        mp3_url = e.links[0].href
        title = date +"-" + e.title
        name = replace_nonalphanumeric(title)


        print( f'{name}')
        print(f'{summary}')
        titleText[title] = summary


        # txt  = os.path.join(  os.path.dirname(os.path.realpath(__file__)), folder, name+".txt")
        # if not os.path.isfile( txt) :
        #     with open(txt, 'w', encoding='utf-8') as txt_file:
        #         txt_file.writelines( [ "\n",  "###"+title+"\n", summary ])
        #
        #
        # print(f'{mp3_url}')
        # resp = requests.get(mp3_url)
        # mp3  = os.path.join(  os.path.dirname(os.path.realpath(__file__)), folder, name+".mp3")
        # if not os.path.isfile(mp3):
        #     with open( mp3 , 'wb') as mp3_file:
        #         mp3_file.write(resp.content)

        print( "titles = ", titleText)
        with open(folder + "/combined_text.txt", 'w', encoding='utf-8') as combined_file:
            for title in sorted( titleText.keys() ):
                print(title)
                combined_file.writelines(["\n", "###" + title + "\n", titleText[title]  ])



down_feed(feed_reallife_french)

