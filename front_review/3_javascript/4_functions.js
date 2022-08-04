// In JavaScript, functions follow this general form:
// (parameters are also commonly called arguments)

function name(parameter1, parameter2, parameter3) {
    //code to be executed
}

// Now let's see several examples!

// EXAMPLE
// Simple function with no input parameters
function hello(){
    console.log("hello world!");
}

// This will just return the function:
hello

// You need to add parenthesis (and any parameters you want) to actually call
// the function into action!
hello()

///////////////////////
// Returning Values //
/////////////////////

// So far we've only been printing out results, but what if we wanted to return
// the results so that we could assign them to a variable, we can use the return
// keyword for this task in the following manner:

// EXAMPLE

// Without Return
function formal(name="Sam",title="Sir"){
    console.log(title+" "+name)
}

//
"Welcome " + formal()
// Welcome undefined


// With a return
function formal(name="Sam",title="Sir"){
    return title+" "+name;
}

//
"Welcome "+formal()
//

var result = formal()///////////////////////
// Returning Values //
/////////////////////

// So far we've only been printing out results, but what if we wanted to return
// the results so that we could assign them to a variable, we can use the return
// keyword for this task in the following manner:

// EXAMPLE

// Without Return
function formal(name="Sam",title="Sir"){
    console.log(title+" "+name)
}

//
"Welcome " + formal()
// Welcome undefined


// With a return
function formal(name="Sam",title="Sir"){
    return title+" "+name;
}

//
"Welcome "+formal()
//

var result = formal()