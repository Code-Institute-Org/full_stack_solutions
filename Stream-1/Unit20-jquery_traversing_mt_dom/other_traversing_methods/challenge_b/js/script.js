//will wait uuntil page ready
 $(document).ready(function(){

    /*when table header is clicked , removes selection class from all other table rows and
      adds the selection class to this table headers row only*/
     $("th").click(function(){
     	$("tr").children().removeClass("selection")
    	$(this).siblings().addClass("selection");

  });
 });

