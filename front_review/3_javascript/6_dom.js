var myHeader = document.querySelector("h1")

function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}


function changeColor() {
    myHeader.style.color = getRandomColor();
}
// Perform the function every 0.5 second
setInterval("changeColor()", 500);