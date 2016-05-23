
//initial piece of writing
var profile = "I am a web developer developing in html css and javascript";
var stops = ["i","am","a","and"]; //words to be removed from profile
//splits profile 
var words = profile.split(" ");
//create function to assign newProfile array and push words into it
function cleanProfile(words,stops) {
var newProfile = [];

for (i=0;i<words.length;i++){
   if (stops.indexOf(words[i].toLowerCase()) < 0) {
       newProfile.push(words[i])
   }
       
}
return newProfile;
}
console.log("New Profile");
//write results of function to console 
console.log(cleanProfile(words,stops));