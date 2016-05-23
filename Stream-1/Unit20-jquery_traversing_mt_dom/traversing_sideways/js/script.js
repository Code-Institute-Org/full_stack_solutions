//waits until page is ready
$(document).ready(function() {
 
//sets current h2 to change color and font-size on mouse enter
$("h2").mouseenter(function(){
	$(this).css('background-color','lightblue');
	$(this).css('font-size','20px');
});
//creates a fadeTo effect on current button on mouseenter
$("button").mouseenter(function(){
	$(this).fadeTo(1000,0.5);
	 
});
//and a fadaTo effent on current button on mouseout
$("button").mouseout(function(){
	$(this).fadeTo(1000,1);
	 
});
//creates slide toggle on paragraph on button click
$("button").click(function(){
	$(this).prev().slideToggle(1000);	 
});
//assigns colour yellow to all links un current paragraph
$("p").click(function(){
	$(this).children('a').css('background-color','yellow');	 
});
//slides down paragrph directly under image when img is clicked 
$("img").click(function(){
	$(this).next().children('p').slideDown();	 
});
//when card is clicked, it is assigned class highlight and
// is highlighted but if clicked again class highlight is toggled off
$(".card").click(function(){
	$(this).toggleClass("highlight");	 
});
//cards not currently seleced will be hidden when select_btn is clicked
$("#select_btn").click(function(){
	$(".card:not(.highlight)").hide();	 
});
//all cards will now be selected
$("#all_btn").click(function(){
	$(".card").show();	 
});
//underlines all h2's amd adds border to the nav
$("h2").addClass("underline");
   $("nav").addClass("border");
   //on stream_btn click, associated stream will be highlighted only
 	$("#stream1_btn").on("click", function() {
 		$(".stream1").removeClass('highlight_stream');
		$(".stream2").removeClass('highlight_stream');
		$(".stream3").removeClass('highlight_stream');
	  	$(".stream1").addClass('highlight_stream');
	});
	$("#stream2_btn").on("click", function() {
		$(".stream1").removeClass('highlight_stream');
		$(".stream2").removeClass('highlight_stream');
		$(".stream3").removeClass('highlight_stream');
	  	$(".stream2").addClass('highlight_stream');
	});
	$("#stream3_btn").on("click", function() {
		$(".stream1").removeClass('highlight_stream');
		$(".stream2").removeClass('highlight_stream');
		$(".stream3").removeClass('highlight_stream');
	  	$(".stream3").addClass('highlight_stream');
	});


}); 
