$(document).ready(function() {
 	//revoves claas makeRed, adds class makeBorder on mouseenter
 	$("button").mouseenter(function(){
 	 $(this).removeClass("makeRed").addClass("makeBoarder");

 	});
 	//reverses above on mouseleave
 	$("button").mouseleave(function(){
 	 $("button").removeClass("makeBoarder").addClass("makeRed");

 	});
 	//toggles paragraphs when either button is clicked
 	$("button").click(function(){
 	 $("p").slideToggle(2000);
 	});

 	//hides/shows  paragraphs when either button is clicked
 	$("button").click(function(){
 	 $("p").hide(2000).show(2000);
 	});
 		//fadeIn and fadoeOut on paragraphs when either button is clicked
 	$("button").click(function(){
 	 $("p").fadeIn().fadeOut();
 	});


}); 

