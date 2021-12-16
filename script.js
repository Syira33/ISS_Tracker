// retrieve all elements needed
let latitudeText = document.querySelector('.latitude');
let longitudeText = document.querySelector('.longitude');
let timeText = document.querySelector('.time');

/* default latitude and longitude. Here lat and long is for "London" */
let lat = 51.505;
let long = -0.09;
let zoomLevel = 8;

// set iss.png image as Marker for current location
const icon = L.icon({
    iconUrl: './img/iss.png',
    iconSize: [90, 45],
    iconAnchor: [25, 94],
    popupAnchor: [20, -86]
  });

// drawing map interface on #map-div
//L.map() creates a Leaftlet map

const map = L.map('map-div').setView([lat, long], zoomLevel);

// add map tiles from Mapbox's Static Tiles API
/* to get Mapbox API accessToken --> https://account.mapbox.com/access-tokens/ (do Signup or SignIn) */

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox/streets-v11',
  tileSize: 512,
  zoomOffset: -1,
  accessToken: 'pk.eyJ1IjoiYW1pcmFoc2FicmluYSIsImEiOiJja3g3bDhqdm0zMzZlMnhxcjVuaWc4b2RlIn0.CBWUG5GBOBCZZ_AnytqgjA'
}).addTo(map);

// adding the Marker to map
const marker = L.marker([lat, long], { icon: icon }).addTo(map);

// findISS() function definition

function findISS() {
    fetch("https://api.wheretheiss.at/v1/satellites/25544")
    .then(response => response.json())
    .then(data => {
      lat = data.latitude.toFixed(2);
      long = data.longitude.toFixed(2);
      // convert seconds to milliseconds, then to UTC format
      const timestamp = new Date(data.timestamp * 1000).toUTCString();
  
      // call updateISS() function to update things
      updateISS(lat, long, timestamp);
    })
    .catch(e => console.log(e));
  }

// updateISS() function definition
function updateISS(lat, long, timestamp) {
    // updates Marker's lat and long on map
    marker.setLatLng([lat, long]);
    // updates map view according to Marker's new position
    map.setView([lat, long]);
    // updates other element's value
    latitudeText.innerText = lat;
    longitudeText.innerText = long;
    timeText.innerText = timestamp;
    
  }

/* call findISS() initially to immediately set the ISS location */
findISS();

// call findISS() for every 10mins
setInterval(findISS, 600000);