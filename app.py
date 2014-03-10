from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

token = os.environ.get('ECHONEST_TOKEN')
if token == None:
  token = open("ECHONEST_TOKEN").read().replace('\n','')

class Ship(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=False)
  capacity = db.Column(db.Integer, unique=False)
  speed = db.Column(db.Integer, unique=False)
  image = db.Column(db.String(120), unique=False)

  def __init__(self, name, capacity, speed, image):
    self.name = name
    self.capacity = capacity
    self.speed = speed
    self.image = image

  def __repr__(self):
    return self.name

@app.route('/search')
def search():
  speed = request.args.get('speed')
  capacity = request.args.get('capacity')
  ships = None
  if (speed and capacity):
    ships = Ship.query.filter(Ship.speed >= int(speed), Ship.capacity >= int(capacity))
  elif speed:
    ships = Ship.query.filter(Ship.speed >= int(speed))
  elif capacity:
    ships = Ship.query.filter(Ship.capacity >= int(capacity))
  else:
    ships = Ship.query.all()
  return render_template('index.html', ships=ships, speed=speed, capacity=capacity)

@app.route('/view/<name>')
def view(name=None):
  ship = Ship.query.filter_by(name=name).first()
  return render_template('view.html', ship=ship)

if __name__ == "__main__":
  app.run(debug=True)