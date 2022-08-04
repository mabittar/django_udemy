// looping example and even

var x = 0;

while (x <= 10) {
    console.log(x);
    // if (x == 5) {
    //     console.log("X is 5!!. Get out!");
    //     break;
    // }
    if (x % 2 == 0) {
        console.log(x + " is even");
    }

    x++;
}