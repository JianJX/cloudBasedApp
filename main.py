import requests
import json
import random
from flask import Flask, render_template, request
from credentials import API_KEY

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/listing')
def listing():
    return render_template('listing.html')

@app.route('/result', methods=['GET'])
def result():
    nearby_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    args = request.args
    category = args.get('category')
    distance = args.get('distance')
    flag = args.get('check')
    lat = args.get('lat')
    lng = args.get('lng')
    radius = str(int(distance) * 1609)
    search_url = "{}location={},{}&radius={}&type=restaurant&keyword={}&key={}".format(nearby_url, lat, lng, radius, category, API_KEY)
    res = requests.get(search_url).json()
    restaurants = res["results"]
    return render_template("result.html", results=restaurants, random_select=flag)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)