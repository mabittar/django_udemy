// Problem 1

// Alert the name and job of the object in terminal

var empolyee = {
    name: "Marcel Bittar",
    age: 39,
    job: "Software Engineer",
    greet: function(){
        alert("Hello, my name is "+this.name + " and I am a " + this.job);
    }
}

// Problem 2
// Print the length name of the object in terminal
var empolyeeLength = {
    name: "Marcel Bittar",
    age: 39,
    job: "Software Engineer",
    greet: function(){
        console.log("Hello, my name is length "+this.name.length);
    }
}

// Problem 3
// Add a method to print the last name of the object in terminal
var empolyeeLength = {
    name: "Marcel Bittar",
    age: 39,
    job: "Software Engineer",
    greet: function(){
        console.log("Hello my last name is: "+this.name.split(" ")[1]);
    }
}