from urllib import request, parse
import json

API_KEY = "AthLEatwKbc-IyBBkeaVPjATmJ3GxG_ALQobFSBuFOTQ8-RHkmPHiGj6XWuRpQdY"

# input information
longitude = -122.019943
latitude = 37.285989
start = "77 Chapel Hill Road Mount Laurel NJ 08054"
destination = "235 Hartford Road Medford NJ 08055"

encodedStart = parse.quote(start, safe='')
encodedDest = parse.quote(destination, safe='')

routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + encodedStart + "&wp.1=" + encodedDest + "&key=" + API_KEY
print(routeUrl)
r = request.Request(routeUrl)
response = request.urlopen(r)

r = response.read().decode(encoding="utf-8")
result = json.loads(r)

itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]

for item in itineraryItems:
    print(item["instruction"]["text"])