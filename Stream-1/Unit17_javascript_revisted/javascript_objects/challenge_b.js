// original profile text
var profile = "I am a web developer developing in html css and javascript";

// stop words to be removed from the profile text
// (to avoid duplication, we only store the lower-case version)
var stops = ["i", "am", "a", "and"];


function cleanProfile(profile, stops) {
    // split profile text into separate words 
    var words = profile.split(" ");

    // Instead of modifying the existing profile, we'll push the non-stop
    // words into a new array
    var newProfile = [];

    for (var i=0; i<words.length; i++){
        // Check if the lower-case version of the word is not in the stops 
        if (stops.indexOf(words[i].toLowerCase()) === -1) {
            newProfile.push(words[i])
        }
     }
     return newProfile;
}


//write results to console 
console.log("Clean profile words:");
console.log(cleanProfile(profile, stops));
