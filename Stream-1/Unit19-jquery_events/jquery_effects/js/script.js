//waits until page is loaded first
$(document).ready(function(){

    //applies colour red to paragraphs when clicked on 
    $("p").click(function(){
        $("p").addClass( "highlight_text");
    });

    //will add lightblue to h2 elements
    $("h2").hover(function(){
        $("h2").addClass( "h2_color");   
    });

    /* This will apply larger font size to the active h2 element 
       by adding the h2_font_size class and remove the h2_font_size
       from all other h2 elements.
       Note that this solution is very repetitive, and later on we'll
       see an easier and more concise way of achieving this.
    */
    $("#hr_html").hover(function(){
        $("#hr_mysql").removeClass("h2_font_size");
        $("#hr_python").removeClass("h2_font_size");
        $("#hr_jquery").removeClass("h2_font_size");
        $("#hr_django").removeClass("h2_font_size");
        $("#hr_css").removeClass("h2_font_size");
        $("#hr_html").addClass("h2_font_size");
    });

    $("#hr_mysql").hover(function(){
        $("#hr_python").removeClass("h2_font_size");
        $("#hr_jquery").removeClass("h2_font_size");
        $("#hr_django").removeClass("h2_font_size");
        $("#hr_css").removeClass("h2_font_size");
        $("#hr_html").removeClass("h2_font_size");
        $("#hr_mysql").addClass("h2_font_size");
    });

    $("#hr_python").hover(function(){
        $("#hr_mysql").removeClass("h2_font_size");
        $("#hr_jquery").removeClass("h2_font_size");
        $("#hr_django").removeClass("h2_font_size");
        $("#hr_css").removeClass("h2_font_size");
        $("#hr_html").removeClass("h2_font_size");
        $("#hr_python").addClass("h2_font_size");
    });

    $("#hr_jquery").hover(function(){
        $("#hr_mysql").removeClass("h2_font_size");
        $("#hr_python").removeClass("h2_font_size");
        $("#hr_django").removeClass("h2_font_size");
        $("#hr_css").removeClass("h2_font_size");
        $("#hr_html").removeClass("h2_font_size");
        $("#hr_jquery").addClass("h2_font_size");

    });
    $("#hr_django").hover(function(){
        $("#hr_mysql").removeClass("h2_font_size");
        $("#hr_python").removeClass("h2_font_size");
        $("#hr_jquery").removeClass("h2_font_size");
        $("#hr_css").removeClass("h2_font_size");
        $("#hr_html").removeClass("h2_font_size");
        $("#hr_django").addClass("h2_font_size");

    });
    $("#hr_css").hover(function(){
        $("#hr_mysql").removeClass("h2_font_size");
        $("#hr_python").removeClass("h2_font_size");
        $("#hr_jquery").removeClass("h2_font_size");
        $("#hr_django").removeClass("h2_font_size");
        $("#hr_html").removeClass("h2_font_size");
        $("#hr_css").addClass("h2_font_size");

    });

    //applies colour black to body body background when mouse  over buttons
    $(".bottom_button").mouseenter(function(){
        $("body").css( "background-color", "black"); 

    });
    //applies colour grey to bodybackground when mouse leaves buttons
    $(".bottom_button").mouseleave(function(){
        $("body").css( "background-color", "#eee"); 


    });

    //uncomment to see example of hide function

     /*$("#button_effects1").click(function(){
        $('#button_effects1').hide('slow');

    });*/


    //adds slideTogggle to buttons to toggle paragraphs open and closed
    $("#button_effects1").click(function(){
        $('#par1').slideToggle('1000');
    });
    $("#button_effects2").click(function(){
        $('#par2').slideToggle('1000');
    });
    $("#button_effects3").click(function(){
        $('#par3').slideToggle('1000');
    });
    $("#button_effects4").click(function(){
        $('#par4').slideToggle('1000');
    });
    $("#button_effects5").click(function(){
        $('#par5').slideToggle('1000');
    });
    $("#button_effects6").click(function(){
        $('#par6').slideToggle('1000');
    });

    //adds fade to when  mouserenter and mouseleave button
    $("#button_effects1").mouseenter(function(){
        $('#button_effects1').fadeTo(1000, 0.5);
    });
    $("#button_effects1").mouseleave(function(){
        $('#button_effects1').fadeTo(1000, 1);
    });

    $("#button_effects2").mouseenter(function(){
        $('#button_effects2').fadeTo(1000, 0.5);
    });
    $("#button_effects2").mouseleave(function(){
        $('#button_effects2').fadeTo(1000, 1);
    });

    $("#button_effects3").mouseenter(function(){
        $('#button_effects3').fadeTo(1000, 0.5);
    });
    $("#button_effects3").mouseleave(function(){
        $('#button_effects3').fadeTo(1000, 1);
    });

    $("#button_effects4").mouseenter(function(){
        $('#button_effects4').fadeTo(1000, 0.5);
    });
    $("#button_effects4").mouseleave(function(){
        $('#button_effects4').fadeTo(1000, 1);
    });

    $("#button_effects5").mouseenter(function(){
        $('#button_effects5').fadeTo(1000, 0.5);
    });
    $("#button_effects5").mouseleave(function(){
        $('#button_effects5').fadeTo(1000, 1);
    });

    $("#button_effects6").mouseenter(function(){
        $('#button_effects6').fadeTo(1000, 0.5);
    });
    $("#button_effects6").mouseleave(function(){
        $('#button_effects6').fadeTo(1000, 1);
    });

});
