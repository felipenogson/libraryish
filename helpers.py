from dotenv import load_dotenv
import os
import re
from googleapiclient.discovery import build  
import random

load_dotenv()
api_key = os.getenv('YOUTUBE_API')
youtube = build('youtube', 'v3', developerKey=api_key)

def search( q:str = '', n:int = 12) -> list:
	''' Search for [q]query on youtube and return a list with the id of the results '''
	request = youtube.search().list( 
		part="snippet", 
		maxResults=n, 
		q=f"audiobook {q}", 
		type="video",
		# relevanceLanguage='',
		videoDuration="long")

	response = request.execute()

	# Extract the video ids from results response 
	ids = []
	for i in response['items']:
		ids.append(i['id']['videoId'])

	return ids

def contentDetails(video_ids:list):
	request = youtube.videos().list( part="snippet,contentDetails,statistics", id=','.join(video_ids))
	response = request.execute()
	items = response['items']

	# Add the max hours content
	for i in items:
		try:
			i['contentDetails']['hours'] = re.search(r'PT(.*?)H', i['contentDetails']['duration']).group(1)
		except:
			i['contentDetails']['hours'] = 'Less than '
		# it delets the tags that have audiobook on it
		# try: 
		# 	i['snippet']['tags'] = random.choices(5, k=[tag for tag in i['snippet']['tags'] if ('audiobook' not in tag) or ('audio' not in tag) ])
		# except: 
		# 	i['snippet']['tags'] = []
	return items