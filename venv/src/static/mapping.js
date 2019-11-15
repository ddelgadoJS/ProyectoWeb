var currRoute;
var map = L.map('map');
L.tileLayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=tctLp8XfyJogfuDP1C2H', {
	attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
}).addTo(map);

start_icon = L.icon({
	iconUrl: 'https://www.mapquestapi.com/staticmap/geticon?uri=poi-red_1.png',
	iconSize: [20, 29],
	iconAnchor: [10, 29],
	popupAnchor: [0, -29]
});

parada_icon = L.icon({
	iconUrl: 'https://www.mapquestapi.com/staticmap/geticon?uri=poi-orange_1.png',
	iconSize: [20, 29],
	iconAnchor: [10, 29],
	popupAnchor: [0, -29]
});

end_icon = L.icon({
	iconUrl: 'https://www.mapquestapi.com/staticmap/geticon?uri=poi-blue_1.png',
	iconSize: [20, 29],
	iconAnchor: [10, 29],
	popupAnchor: [0, -29]
});

function createRoute(ruta){
	var color;
	var r = Math.floor(Math.random() * 150 + 50)-50;
	var g = Math.floor(Math.random() * 150 + 50)-50;
	var b = Math.floor(Math.random() * 150 + 50)-50;
	r = (r).toString(16);
	g = (g).toString(16);
	b = (b).toString(16);
	colorHex = "#"+r+g+b;														
	
	currRoute = L.Routing.control({
		  waypoints: ruta,
		  collapsible: true,
		  waypointMode: "snap",
		  addWaypoints: false,
		  draggableWaypoints: false,
		  createMarker: function() { return null; },
		  lineOptions:{
			styles: [
				{color:colorHex}
				]
		  }
		}).addTo(map);
	document.getElementById('map').children[2].children[1].style="display:none;";
}

function consultaRuta(tabla){
	return JSON.parse((tabla).replace(/&(l|g|quo)t;/g, function(a,b){
		return {
			l   : '<',
			g   : '>',
			quo : '"'
		}[b];
	}));
}