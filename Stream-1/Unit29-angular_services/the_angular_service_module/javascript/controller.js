angular.module('collegeControllers',[]).controller('StudentController',function($scope,StudentService) {

//  returns greetings and student fullname
  $scope.student = StudentService.getStudent();
	$scope.greeting = function(){
		return "Greetings " + $scope.student.fullName();
	}
});
 