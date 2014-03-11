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
  search = request.args.get('search')
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
