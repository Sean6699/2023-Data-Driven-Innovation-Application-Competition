import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyAz1SL-ycn4SNhtCGFejPRvGIvykYV22t0')
radius = 1000
key_word_list = ['餐廳', '酒吧', '景點', '購物']
location_list =  [(24.98, 121.53), (24.99, 121.48), (25.003, 121.51),
(24.98, 121.56), (25.005, 121.61), (25.01, 121.64), (25.02, 121.60),
(24.93, 121.37), (24.96, 121.34), (24.97, 121.44), (24.964, 121.34),
(24.98, 121.41), (25.184, 121.65), (25.20, 121.61), (25.01, 121.44),
(25.08, 121.65), (25.09, 121.81), (25.02, 121.72), (25.00, 121.83),
(25.05, 121.90), (24.78, 121.54), (24.91, 121.72), (25.06, 121.49),
(25.03, 121.43), (25.05, 121.41), (25.10, 121.34), (25.09, 121.47),
(25.09, 121.43), (25.14, 121.41), (25.20, 121.45), (25.25, 121.51)]

results = []
seen_names = set()

for keyword in key_word_list:
    for lat, lng in location_list:
        location = (lat, lng)
        result = gmaps.places_nearby(location=location, radius=radius, keyword=keyword, type=keyword, language='zh-tw')
        for place in result['results']:
            if 'rating' in place and place['rating'] > 4:
                name = place['name']
                if name not in seen_names:
                    rating = place['rating'] 
                    address = place['vicinity'] 
                    opening_hours = place['opening_hours'] if 'opening_hours' in place  else '無營業時間資訊'
                    open_now = opening_hours['open_now'] if isinstance(opening_hours, dict) and 'open_now' in opening_hours else None
                    open_now_int = int(open_now) if isinstance(open_now, bool) else None
                    results.append((name, rating, address, open_now_int))
                    seen_names.add(name)

df = pd.DataFrame(results, columns=['地點', '評分', '地址', '是否營業中'])
print(df)
