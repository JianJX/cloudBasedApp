def geo_search():
    full_url = geo_url + "address=" + street_f + ',+' + city_f + ',+' + state_f + API_KEY
    response = requests.get(full_url)
    data = response.json()
    r = data["results"][0]["geometry"]["bounds"]["northeast"]
    lat = r["lat"]
    lng = r["lng"]
    nearby_search(lat, lng, distance, food_category)
        
def nearby_search(lat, lng, distance, food_category):
    coordinates = 'location=' + str(lat) + ',' + str(lng)
    radius = "&radius=" + str(int(distance) * 1609)
    search_type = "&type=restaurant"
    keyword = "&keyword=" + (food_category.replace(' ', '+'))

    full_url = search_url + coordinates + radius + search_type + keyword + API_KEY
    response = requests.get(full_url)
    data = response.json()
    r = data["results"]