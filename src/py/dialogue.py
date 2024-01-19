
import pytest
import requests
from bs4 import BeautifulSoup , Tag
from pprint import pprint
from playwright.sync_api import Page
from typing import Callable




def download_dialogue_mp3(text:str):
    pass
    '''
        1. find h2 with "dialoguue:"
        2.  first : .map_download
    '''
    # data = requests.get(url)
    # with open( 't.html' , 'w', encoding='utf-8') as f:
    #     f.write(data.text)
    # # url1 = 'https://www.podcastfrancaisfacile.com/dialogue/fle-parler-du-week-end-fle.html'
    # # page.goto(url1)
 
    # #pprint(data.text)
    soup = BeautifulSoup(text, 'html.parser')
    #print(soup.prettify())
    elems  = soup.find_all('div.mbMiniPlayer' )#'map_download' )
    elems  = soup.find_all('div.mbMiniPlayer' )#'map_download' )
    dialogue_mp3 = soup.find_all( lambda tag: 
        tag.name =='a' 
        and len(tag.attrs)>0
        and 'mp3' in tag['href']
        and 'uploads' in tag['href']
        and 'dialogue' in tag['href']
        #and 'download' in tag.attrs 
        # and tag["download"].startswith('dialogue')
        )

    if len(dialogue_mp3) == 1:
        dialogure_mp3_url = dialogue_mp3[0]['href']
        res = requests.get(dialogure_mp3_url)
        with open('mp3.mp3', 'wb') as f:
            f.write(res.content)


    else:
        print(" error: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def download_dialogue_transcription(text:str , file_path: str):
    '''
    find 
    .fusion-toggle-has-divider

    contains : transcription
    '''
    #https://stackoverflow.com/questions/33833881/is-it-possible-to-type-hint-a-lambda-function
    attr_func : Callable[ [Tag], bool]  = lambda tag: tag.name =='div' 
        and tag.find('div.panel-heading') and '' tag.find('div.panel-heading').text


    class_group = 'panel-group'
    class_heading = 'panel-heading'
    class_content = 'panel-collapse'



    soup = BeautifulSoup(text, 'html.parser')
    elems = soup.find_all('div', {class_} )

def download(url:str )->None:
    data = requests.get(url)
    with open( 't.html' , 'w', encoding='utf-8') as f:
        f.write(data.text)
    # url1 = 'https://www.podcastfrancaisfacile.com/dialogue/fle-parler-du-week-end-fle.html'
    # page.goto(url1)
    download_dialogue_mp3(data.text)
    download_dialogue_transcription(data.text)









if __name__ == '__main__':
    url1 = 'https://www.podcastfrancaisfacile.com/dialogue/fle-parler-du-week-end-fle.html'
    download(url=url1)