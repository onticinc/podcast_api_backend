from bs4 import BeautifulSoup
import requests
from flask import Flask, request, jsonify
import json

source = requests.get('https://feeds.simplecast.com/T8TzwY_T').text
soup = BeautifulSoup(source, 'lxml')

item_results = []

# for item in soup.findAll('item'):

class Item:
    def __init__(
        self, 
        site_title,
        itunes_episode,
        itunes_title,
        itunes_author,
        itunes_duration,
        itunes_explicit,
         ) -> None:
    pass


for item in soup.findAll('item'):

    site_title = item.find('title').text
    itunes_episode = item.find('itunes:episode').text
    itunes_title = item.find('itunes:title').text
    itunes_author = item.find('itunes:author').text
    itunes_duration = item.find('itunes:duration').text
    itunes_explicit = item.find('itunes:explicit').text
    itunes_summary = item.find('itunes:summary').text
    cover_art = item.find('itunes:image')
    media = item.find('enclosure')['url']

    item_results.append({
        
        'site_title': site_title, 
        'itunes_episode': itunes_episode, 
        'itunes_title': itunes_episode, 
        'itunes_author': itunes_author, 
        'itunes_duration': itunes_duration, 
        'itunes_explicit': itunes_explicit, 
        'itunes_summary': itunes_summary, 
        'cover_art': cover_art, 
        'media':media,
    })

    # def store_data(results):
    #     return(results)
    # # print(item_results)

try:

   None

except Exception as e:

    site_title = None
    itunes_episode = None
    itunes_title = None
    itunes_author = None
    itunes_duration = None
    itunes_explicit = None
    cover_art = None
    media = None

print(item_results)

for i in range(len(item_results)):
    print(item_results[i][
        'site_title'
        'itunes_episode'
        'itunes_title'
        'itunes_author'
        'itunes_duration'
        'itunes_explicit'
        'itunes_summary'
        'cover_art'
        'media'
    ])


# for i in range(100):
#     print(type(item_results[i]))
#     print(item_results[i]['itunes_summary'])
