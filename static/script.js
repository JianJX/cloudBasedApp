function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  const category = document.getElementById("category").value;
  const distance = document.getElementById("distance").value;
  if (document.getElementById("random_select").checked) {
    var check = 'true';
  } else {
    var check = 'false';
  }
  var url = '/nearbyResult?category=' + category + "&distance=" + distance + "&lat=" + position.coords.latitude + "&lng=" + position.coords.longitude + "&check=" + check; 
  //url = '/nearbySearch?category=' + category + "&distance=" + distance + "&lat=" + position.coords.latitude + "&lng=" + position.coords.longitude + "&check=" + check; 
  window.location.href = url;
}
