import json, urllib.request, time


#A first JSON request to retrieve the name of all the astronauts currently in space.
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
astronaut = json.loads(response.read())
print("There are currently about " + str(astronaut["number"]) + " astronauts in space:")
print("")

people = astronaut["people"]

for p in people:
  print(p["name"] + " on board of " + p["craft"])


while True:
  #A JSON request to retrieve the current longitude and latitude of the IIS space station (real time)  
  url = "http://api.open-notify.org/iss-now.json"
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
    
  #Let's extract the required information
  location =result["iss_position"]
  lat = location["latitude"]
  lon = location["longitude"]
    
  #Output on screen
  print("\nLatitude: " + str(lat))
  print("Longitude: " +str(lon))
  
  #refresh position every 5 seconds
  time.sleep(5)

