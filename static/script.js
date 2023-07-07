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
  if (document.getElementById("open_now").checked) {
    var open_now = 'true';
  } else {
    var open_now = 'false';
  }
  var url = '/nearbyResult?category=' + category;
  url += "&distance=" + distance;
  url += "&lat=" + position.coords.latitude + "&lng=" + position.coords.longitude;
  url += "&check=" + check;
  url += "&open=" + open_now;
  window.location.href = url;
}
