var roster = []

function addName(){
    var newName = prompt("Enter a new name:");
    roster.push(newName);
}

function removeName(){
    var nameToRemove = prompt("Enter a name to remove:");
    var index = roster.indexOf(nameToRemove);
    roster.splice(index, 1);
}

function printRoster(){
    console.log(roster);
}

function clearRoster(){
    roster = [];
}

function printRosterLength(){
    console.log(roster.length);
}

var start = prompt("Would you like to start the roster? (y/n)");
var request = "empty";

if (start === 'y'){
    while (request !== "quit"){
        request = prompt("Would you like to add, remove, print, clear, length or quit?");
    
    if (request === "add"){
        addName();
    }else if(request === "remove"){
        removeName();
    }else if(request === "print"){
        printRoster();
    }else if(request === "clear"){
        clearRoster();
    }else if(request === "length"){
        printRosterLength();
    }else {
        alert("Not recognized. Please reload again.");
        // request = "quit";
    }
}

}
alert("Thanks for using the roster!");