// Note: This example requires that you consent to location sharing when
 // prompted by your browser. If you see the error "The Geolocation service
 // failed.", it means you probably did not give permission for the browser to
 // locate you.
 var map, infoWindow;
 function initMap() {
   map = new google.maps.Map(document.getElementById('map'), {
     center: {lat: -34.397, lng: 150.644},
     zoom: 12
   });
   infoWindow = new google.maps.InfoWindow;
   $("#latitude").val("-34.397");
   $("#longitude").val("150.644");

 // Try HTML5 geolocation.
   if (navigator.geolocation) {
     navigator.geolocation.getCurrentPosition(function(position) {
       var pos = {
         lat: position.coords.latitude,
         lng: position.coords.longitude
       };
       $("#latitude").val(pos.lat);
       $("#longitude").val(pos.lng);
       $.cookie("latitude", pos.lat);
       $.cookie("longitude", pos.lng);
       GetAddress();
       var marker = new google.maps.Marker({
       position: pos,
       map: map,
       draggable:true,
       title: 'Location Found'
     });
       marker.setMap(map);
var infowindow = new google.maps.InfoWindow({
  content:"Your location"
  });

infowindow.open(map,marker);

       if ($.cookie("latitude") && $.cookie("longitude")) {
        $.ajax({
          url: SRC.BASE_URI + "hospital/nearby/?latitude=" + $.cookie("latitude") + "&longitude=" + $.cookie("longitude"),
          success: function(response) {
            data = response.items
            $.each(data, function(key, value) {
              var marker = new google.maps.Marker({
                position: {lat: value.latitude, lng: value.longitude},
                map: map,
                draggable: false,
                title: value.name,
                
              });
              marker.setMap(map);
              var infowindow = new google.maps.InfoWindow({
                content:value.name
                });

              infowindow.open(map,marker);
            });
          }
        });
       }
      google.maps.event.addListener(marker, 'drag', function(event){
        $("#latitude").val(event.latLng.lat());
        $("#longitude").val(event.latLng.lng());
        GetAddress();
      });
       infoWindow.open(map);
       map.setCenter(pos);
     }, function() {
       handleLocationError(true, infoWindow, map.getCenter());
     });
   } else {
     // Browser doesn't support Geolocation
     handleLocationError(false, infoWindow, map.getCenter());
   }
 }

 function handleLocationError(browserHasGeolocation, infoWindow, pos) {
   infoWindow.setPosition(pos);
   infoWindow.setContent(browserHasGeolocation ?
                         'Error: The Geolocation service failed.' :
                         'Error: Your browser doesn\'t support geolocation.');
   infoWindow.open(map);
 }

 function GetAddress() {
     var latlng = new google.maps.LatLng($("#latitude").val(), $("#longitude").val());
     var geocoder = new google.maps.Geocoder();
     geocoder.geocode({'latLng': latlng}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        if (results[1]) {
          $("#formatted_address").val(results[0].formatted_address);
        }
      }
     })
  }
