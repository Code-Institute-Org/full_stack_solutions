//wait until page is ready
$(document).ready(function() {
 
 		//sets <a> element within paragraph  to yellow  
		$("p").click(function(){
		$(this).children("a").css("background-color", "yellow"); /* returns all the <a> child elements that are 
																	within this paragraph*/

	});

}); 
