// JavaScript Objects is like dict in Python or key-value pairs.

var myNewO = {a: "hello", b: [1, 2, 3], c:{inside:["a", "b", "c"]}};

var myB = myNewO["c"][1];


myNewO["a"] = "goodbye";

console.dir(myNewO);


for (var key in myNewO){
    if (key === "a"){
        console.log(key);
    }
}


var simpleObj = {
    name: "Marcel",
    greet: function(){
        console.log("Hello, my name is "+this.name);
    }
}
console.log(simpleObj["name"]);

// execute the greet function
simpleObj.greet();

// log greet function
simpleObj.greet;