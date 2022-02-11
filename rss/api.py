from dotenv import load_dotenv
import os 
load_dotenv()


TOKEN = os.getenv('API_KEY')



url = 'https://api.simplecast.com/podcasts/:podcast_id/episodes?limit=12&offset=0'

headers = {

}

r = requests.get(url)
