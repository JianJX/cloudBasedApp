import requests
import json
import random
from flask import Flask, render_template, request
from google.cloud import datastore
from credentials import API_KEY

client = datastore.Client()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/nearbySearch')
def nearbySearch():
    return render_template('nearbySearch.html')

@app.route('/placeSearch')
def placeSearch():
    return render_template('placeSearch.html')

@app.route('/nearbyResult', methods=['GET'])
def nearbyResult():
    nearby_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    args = request.args
    category = args.get('category')
    distance = args.get('distance')
    flag = args.get('check')
    lat = args.get('lat')
    lng = args.get('lng')
    radius = str(int(distance) * 1609)
    full_url = "{}location={},{}&radius={}&type=restaurant&keyword={}&key={}".format(nearby_url, lat, lng, radius, category, API_KEY)
    res = requests.get(full_url).json()
    restaurants = res["results"]
    return render_template("nearbyResult.html", results=restaurants, random_select=flag)

@app.route('/placeResult', methods=['GET'])
def placeResult():
    place_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    args = request.args
    restaurant_name = args.get('phone')
    full_url = "{}input=%2B1{}&inputtype=phonenumber&types=restaurant&key={}".format(place_url, restaurant_name, API_KEY)
    res = requests.get(full_url).json()
    if res['candidates'] == []:
        return render_template("placeResult.html", results=[])

    pid = res['candidates'][0]['place_id']
    detail_url = "https://maps.googleapis.com/maps/api/place/details/json?place_id={}&key={}".format(res['candidates'][0]['place_id'], API_KEY)
    res = requests.get(detail_url).json()
    restaurant = []
    restaurant.append(res['result']['vicinity'])
    restaurant.append(res['result']['name'])
    restaurant.append(pid)
    return render_template("placeResult.html", results=restaurant)

@app.route('/listing', methods=['GET'])
def listing():
    return render_template("listing.html")

@app.route('/listingResult', methods=['POST'])
def listingResult():
    data = request.form
    pid = data['pid']
    name = data['name']
    addr = data['addr']
    price = data['price']
    period = data['period']
    detail = data['detail']
    new_listing = datastore.entity.Entity(key=client.key('listings'))
    new_listing.update(
        {
            'pid': pid,
            'name': name,
            'addr': addr,
            'price': int(price),
            'period': int(period),
            'detail': detail
        }
    )
    try:
        client.put(new_listing)
        return render_template("listingResult.html", res="Listing success")
    except:
        return render_template("listingResult.html", res="Listing failed")

@app.route('/viewListings', methods=['GET'])
def viewListings():
    listings = []
    query = client.query(kind="listings")
    results = list(query.fetch())
    for item in results:
        listing = []
        listing.append(item['name'])
        listing.append(item['addr'])
        listing.append(item['price'])
        listing.append(item['detail'])
        listings.append(listing)
    return render_template("viewListings.html", listings=listings)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)