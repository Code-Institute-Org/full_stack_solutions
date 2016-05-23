//create service
angular.module('collegeServices',[]).factory('StudentService',function() {
// create a student object
  var student = {
        firstName: "Rich",
        lastName: "Richie",
        fees: 500,
        subjects: [{
            name: 'Physics',
            marks: 70
        }, {
            name: 'Chemistry',
            marks: 80
        }, {
            name: 'Math',
            marks: 65
        }, {
            name: 'English',
            marks: 75
        }, {
            name: 'Hindi',
            marks: 67
        }],
        fullName: function () {
            var studentObject;
            studentObject = student;
            return studentObject.firstName + " " + studentObject.lastName;
        }
    };
    // return student object
    return { getStudent: function(){
        return student}
        };
    
}); 