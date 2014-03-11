from flask import Flask
from flask import render_template
from flask import request

import os
import httplib
import urllib
import json

app = Flask(__name__)

class Song():
  def __init__(self, name, artist):
    self.name = name
    self.artist = artist

  def __repr__(self):
    return self.name

# token = os.environ.get('ECHONEST_TOKEN')
# if token == None:
#   token = open("ECHONEST_TOKEN").read().replace('\n','')
token = "FUFNWYIA18AB8IL8B"

@app.route('/')
def index():
  search = request.args.get('search')
  print(search)
  if search == None:
    search = ""

  # data=json.load(urllib2.urlopen("http://developer.echonest.com/api/v4/playlist/basic?api_key="+key+"&artist="+"artist"+"&format=json&results=20&type=artist-radio"))
  # data=json.load(urllib2.urlopen("http://developer.echonest.com/api/v4/playlist/basic?api_key="+key+"&genre="+"artist"+"&format=json&results=20&type=genre-radio"))
  # data=json.load(urllib2.urlopen("http://developer.echonest.com/api/v4/playlist/basic?api_key="+key+"&song="+"artist"+"&format=json&results=20&type=song-radio"))

  connection = httplib.HTTPConnection('developer.echonest.com')
  connection.request('GET', '/api/v4/playlist/basic?api_key={0}&artist={1}&format=json&results=10&type=artist-radio'.format(token, urllib.quote(search)))
  response = connection.getresponse()
  songs_dictionary = json.loads(response.read().decode('utf-8'))['response'].get('songs')
  if songs_dictionary == None:
    songs_dictionary = []
  songs = []
  for song_details in songs_dictionary:
    songs.append(Song(song_details['title'], song_details['artist_name']))
  return render_template('index.html', songs = songs, search = search)

@app.route('/<name>')
def view(name=None):
  return render_template('index.html', songs = None)

if __name__ == "__main__":
  app.run(debug=True)
