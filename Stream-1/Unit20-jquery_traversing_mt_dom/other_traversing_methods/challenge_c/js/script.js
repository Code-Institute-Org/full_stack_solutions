//waits until page is ready
$(document).ready(function(){
  
//will display rgb value of selected panel in the reset panel
 $(".theButton").click(function(){
    var col = $(this).css('background-color');
  $('.superButton').text( col);

   });
});



