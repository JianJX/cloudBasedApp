function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  var category = document.getElementById("category").value;
  var distance = document.getElementById("distance").value;
  url = 'http://127.0.0.1:8080/result?category=' + category + "&distance=" + distance + "&lat=" + position.coords.latitude + "&lng=" + position.coords.longitude; 
  //url = 'https://ethereal-reef-384100.uw.r.appspot.com/search?category=' + category + "&distance=" + distance + "&lat=" + position.coords.latitude + "&lng=" + position.coords.longitude; 
  window.location.href = url;
}

