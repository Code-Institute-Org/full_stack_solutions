//waits until page is loaded first
$(document).ready(function(){

    //applies colour red to paragraphs when clicked on 
    $("p").click(function(){
        $("p").addClass("highlight_text");
    });

    /* this will add lightblue to h2 elements and will apply larger font size to the active h2 element 
    by adding the h2_font_size class but 
    not the other h2 elements by removing class h2_font_size from them*/
    $("h2").hover(function(){
        $("h2").addClass("h2_color");
        $("h2").removeClass("h2_font_size");
        $(this).addClass("h2_font_size");
    });

    //applies colour black to body background when mouse enters over buttons
    $(".bottom_button").mouseenter(function(){
        $("body").css( "background-color", "black"); 
    });

    //applies colour grey to body background when mouse leaves buttons
    $(".bottom_button").mouseleave(function(){
        $("body").css( "background-color", "#eee"); 
    });
});
