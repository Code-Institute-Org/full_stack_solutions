
//creates variable body and appends paragraph with text
var body = d3.selectAll("body")

body.append("p").text("I Love Data")

body.append("p").text("I Love Data")

body.append("p").text("I Love Data")


//creates variable myDv and appends paragraph with text to it
var myDiv = d3.selectAll("div")

myDiv.append("p").text("Paragraph inside the Div")
//assigns background text and border styles yo myDiv
myDiv.attr("style", "background-color:#ddd; border:solid 4px black")

//adds class smallBox, then removes it before adding red class
myDiv.classed("smallBox" , true);	

myDiv.classed("smallBox", false		);

myDiv.classed("red", true);

//this allows for style background-color to be applied to myDiv
myDiv.attr("style","background-color: red")






