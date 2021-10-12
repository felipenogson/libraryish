from flask import Flask, render_template, session
from config import Config
# from helpers import search, contentDetails
import pickle
import random
import json

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
	# Este codigo es para usar los helpers y el api de youtube
	# ids = search(n=99)
	# ids = random.choices(ids, k=12)
	# items = contentDetails(ids)

	objects = []
	pickle_file = open('data.py', 'rb')
	while True:
		try:
			objects.append(pickle.load(pickle_file))
		except EOFError:
			break
	pickle_file.close()

	items = objects[1]
	items = random.choices(items, k=12)

	return render_template('index.html', items=items)

@app.route("/book_details/<videoId>")
def book_details(videoId):
	# Este codigo es para usar los helpers y el api de youtube
	# video_details = contentDetails([videoId])[0]

	objects = []
	pickle_file = open('data.py', 'rb')
	while True:
		try:
			objects.append(pickle.load(pickle_file))
		except EOFError:
			break
	pickle_file.close()

	items = objects[1]
	
	video_details = [ x for x in items if x['id'] == videoId][0]
	return render_template('book_details.html', video_details=video_details)

@app.route("/shelf")
def shelf():
	return render_template('shelf.html')

@app.route("/player")
def player():
	return render_template('player.html')