var array1 = ["A", "B", "C"];

// iterate over the array
for (var i = 0; i < array1.length; i++) {
  console.log(array1[i]);
}

for (letter in array1){
    console.log(array1[letter]);
}

array1.forEach(function(letter){
    console.log(letter);
});

array1.forEach(alert);

function addAwesome(name){
    return name+" is awesome!";
}

var topics = ["Python", "Django", "FastAPI"];

topics.forEach(addAwesome);
