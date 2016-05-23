
//creat student object
var student = {     firstName: 'Sean',
                    lastName: 'Citizen',
                    age: 21,
                    subjects: [{name: 'Physics', marks: 70}, 
                               {name: 'Chemistry',marks: 80}, 
                               {name: 'Math',marks: 65}, 
                               {name: 'English',marks: 75}, 
                               {name: 'Hindi',marks: 67}],
                fullName: function() {
                    return this.firstName + " "+ this.lastName
                        },
                        //add to aGrades function
                aGrades: function() {
                    for (i=0; i<student.subjects.length;i++) {
                        if (student.subjects[i].marks >= 75) {
                          //print out results
                        console.log("A Grades achieved in: "  + student.subjects[i].name);
                        }
                    }
                    
                }
        }
        //execute function
student.aGrades();