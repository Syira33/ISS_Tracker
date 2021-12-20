import json, urllib.request, time
import webbrowser

f = open('index.html','w')

message = """<html>

  <head>
    <title>ISS Location Tracker</title>
    <link rel="stylesheet" href="styles.css" type="text/css" />
    <!-- CSS for our Map (Mandatory) -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css" integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ==" crossorigin="" />
  </head>
  <body>

    <div>
        <h1>ISS Location Tracker</h1>
  
        <!-- Map goes here -->
        <div id="map-div">
  
        </div>
  
        <!-- Details about ISS -->
        <div id="details">
          <!-- Time -->
          <div>
            Time:
            <span class="time"></span>
          </div>
          <!-- Latitude -->
          <div>
            Latitude:
            <span class="latitude"></span>
          </div>
          <!-- Longitude -->
          <div>
            Longitude:
            <span class="longitude"></span>
          </div>
          
        </div>
        <p 
      </div>


    <!-- Javascript for the Map -->
    <script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js" integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew==" crossorigin=""></script>
    <script src="script.js" type="text/javascript"></script>
  </body>

</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('index.html')

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

