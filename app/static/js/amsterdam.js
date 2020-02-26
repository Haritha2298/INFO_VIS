// LEAFLET.JS
//set up map of amsterdam
// var map = L.map('map', {
//     scrollWheelZoom: false

// }).setView([52.3667, 4.8945], 13);

// // put mapbox layer on 
// L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
//     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//     maxZoom: 18,
//     id: 'mapbox/streets-v11',
//     tileSize: 512,
//     zoomOffset: -1,
//     accessToken: 'pk.eyJ1Ijoibmlsc2xlaCIsImEiOiJjazZ1bDN0OWEwNjUwM21vYTB6Nmk3a3ZpIn0.mCcdD-MMyecijCUrRJKNCg'
// }).addTo(map);

//MAPBOX.JS
mapboxgl.accessToken = 'pk.eyJ1Ijoibmlsc2xlaCIsImEiOiJjazczNHVscGwwOG12M3BqdDZieHJhMW82In0.c-i1H2T6u3vjmj4WY_D2mA'
    
//Setup mapbox-gl map
var map = new mapboxgl.Map({
  container: 'map', // container id
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [4.8945, 52.3667],
  zoom: 13,
    
});

map.addControl(new mapboxgl.NavigationControl());
map.scrollWheelZoom.disable();

// create some markers
var geojson = [
  {
    type: 'Feature',
    geometry: {
      type: 'Point',
      coordinates: [5, 53]
    }
  },
  {
    type: 'Feature',
    geometry: {
      type: 'Point',
      coordinates: [4.5, 52.1]
    }
  }
];

var myLayer = L.mapbox.featureLayer().setGeoJson(geojson).addTo(map);


// // add svg element to leaflet overlay pane
// var svg = d3.select(map.getPanes().overlayPane).append("svg");

// var g = svg.append("g").attr("class", "leaflet-zoom-hide");

// // attempt to put a layer on the map with amsterdam geo json file
// // // put geoJson of Amsterdam over it
// // d3.json("amsterdam.json", function(error, collection) {
// //     if (error) throw error;
// // })

// // // function to render d3 polygon to leaflet polygon
// // function projectPoint(x, y) {
// //     var point = map.latLngToLayerPoint(new L.LatLng(y, x));
// //     this.stream.point(point.x, point.y);
// // }

// // // convert geoJSON to svg
// // var transform = d3.geo.transform({point, projectPoint}),
// //     path = d3.geo.path().projection(transform);

// // var feature = g.selectAll("path")
// //     .data(collection.features)
// //     .enter().append("path");

// // feature.attr("d", path);

// // var bounds = path.bounds(collection),
// //     topLeft = bounds[0],
// //     bottomRight = bounds[1];

// // // set dimension of svg
// // svg.attr("width", bottomRight[0] - topLeft[0])
// //    .attr("height", bottomRight[1] - topLeft[1])
// //    .style("left", topLeft[0] + "px")
// //    .style("top", topLeft[1] + "px");

// // g.attr("transform", "translate(" + -topLeft[0] + "," + -topLeft[1] + ")");

// // create a fisheye distortion as magnifying glass
// var fisheye = d3.fisheye.circular()
//     .radius(100)
//     .distortion(5);

// var lens = svg.append('circle')
//     .attr('class', 'lens')
//     .attr('fill-opacity', 0.1)
//     .attr('r', fisheye.radius());

// // set bounds of svg
// svg .attr("width", 1300)
//     .attr("height", 650)
//     //.style("left", topLeft[0] + "px")
//     //.style("top", topLeft[1] + "px");

// g   .attr("transform", "translate(" + 650 + "," + 1108 + ")");



// // on mousemove move the fisheye over map
// svg.on('mousemove', function() {
//     fisheye.focus(d3.mouse(this));

//     const mouseX = d3.mouse(this)[0];
//     const mouseY = d3.mouse(this)[1];
//     const r = fisheye.radius();

//     lens.attr('cx', mouseX)
//         .attr('cy', mouseY)
// });
