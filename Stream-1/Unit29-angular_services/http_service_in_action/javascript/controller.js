angular.module('collegeControllers',[]).controller('StudentController',function($scope,StudentService) {
//  
	
  $scope.student = StudentService.getStudent();
	$scope.greeting = function(){
		return "Greetings " + $scope.student.fullName();
	}
});

angular.module('collegeControllers')
.controller('RemoteStudentController',function($scope,RemoteStudentService) 
{
      //  pulls data from json file
        $scope.student = {};
        RemoteStudentService.getStudent()
                        .then( function(result) {
                              //promise complete
                              $scope.student=result.data;
                              })
                        //if error occurs getting data
                        .catch( function(error) { console.log('error', error)});
        
        //returns greeting with stundent first and last name 
        $scope.greeting = function(){
                return "Greetings " + $scope.student.firstName + " " + $scope.student.lastName;
        }
        
        $scope.showResults = function(){
        return ($scope.results ? $scope.results=false : $scope.results=true)
        }
        //applys filter to output results over 74 
  $scope.aGradeFilter = function (subject) {
            return (subject.marks > 74);
  }
});
 