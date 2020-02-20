// function to draw the amsterdam map
// function draw(geo_data) {
//     "use strict";
//     var margin = 75,
//         width = 1400-margin,
//         height = 600-margin;

//     var svg = d3.select("#geoMap")
//                 .append("svg")
//                 .attr("width", width + margin)
//                 .attr("height", height + margin)
//                 .append("g")
//                 .attr("class", "map");

//     var projection = d3.geo.mercator()
//                            .scale(150)
//                            .translate( [width / 2, height / 1.5]);
    
//     var path = d3.geo.path().projection(projection);

//     var map = svg.selectAll('path')
//                  .data(geo_data.features)
//                  .enter()
//                  .append('path')
//                  .attr('d', path)
//                  .style('fill', 'lightBlue')
//                  .style('stroke', 'black')
//                  .style('stroke-width', 0.5);
// };

// var adamMap = d3.json("../data/world_countries.json");

// d3.json("../data/world_countries.json", draw);

var adamMap = L.map('leafletMap').setView([52.3667, 4.8945], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1Ijoibmlsc2xlaCIsImEiOiJjazZ1bDN0OWEwNjUwM21vYTB6Nmk3a3ZpIn0.mCcdD-MMyecijCUrRJKNCg'
}).addTo(adamMap);