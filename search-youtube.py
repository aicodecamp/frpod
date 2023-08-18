
# pip install --upgrade google-api-python-client

from dotenv import load_dotenv
import os
import googleapiclient.discovery
import pprint

load_dotenv()


def search():
    api_service_name = 'youtube'
    api_version = 'v3'
    my_api_key = os.environ.get('youtube_key')

    youtube = googleapiclient.discovery.build(api_service_name,
                                              api_version,
                                              developerKey= my_api_key)
    request = youtube.search().list(
        part = 'snippet',
        q='Whistling Diesel',
        maxResults = 10,
        order = 'date',
        type = 'video'
    )

    response = request.execute()

    pprint.pprint(response)



search()