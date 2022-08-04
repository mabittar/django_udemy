$('h1').click(function() {
    console.log('clicked')
})

$('h2').click(function() {
    $(this).text('Text was changed after click')
})

// for other events see:
// https://api.jquery.com/category/events/

$('input').eq(0).keypress(function() {
    $('h2').toggleClass('turnBlue');
})


// see console log for which event was triggered at which attribute
$('input').eq(0).keypress(function(event) {
    if (event.which === 13) {
        $('h2').toggleClass('turnRed');
    }
})

$('h1').on('mouseenter', function() {
    $(this).css('color', 'red')
})

$('input').eq(1).on("click",function(){
  $(".container").fadeOut(3000) ;
})