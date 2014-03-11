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

token = os.environ.get('ECHONEST_TOKEN')
if token == None:
  token = open("ECHONEST_TOKEN").read().replace('\n','')

@app.route('/')
def index():
#data=json.load(urllib2.urlopen("http://developer.echonest.com/api/v4/playlist/basic?api_key="+key+"&artist="+"artist"+"&format=json&results=20&type=artist-radio"))
#data=json.load(urllib2.urlopen("http://developer.echonest.com/api/v4/playlist/basic?api_key="+key+"&genre="+"artist"+"&format=json&results=20&type=genre-radio"))
#data=json.load(urllib2.urlopen("http://developer.echonest.com/api/v4/playlist/basic?api_key="+key+"&song="+"artist"+"&format=json&results=20&type=song-radio"))
  connection = httplib.HTTPConnection('developer.echonest.com')
  artist = urllib.quote("Britney Spears")
  connection.request('GET', '/api/v4/artist/similar?api_key={0}&name={1}'.format(token, artist))
  response = connection.getresponse()
  print(response.read().decode())
  return render_template('index.html', songs = None)

@app.route('/<name>')
def view(name=None):
  return render_template('index.html', songs = None)

if __name__ == "__main__":
  app.run(debug=True)
