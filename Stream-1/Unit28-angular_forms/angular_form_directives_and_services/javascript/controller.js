angular.module('formControllers',[])
  //create controller
    .controller('RegisterController',function($scope, $location) {
        $scope.register = {};
        //sets submitted status to false
        $scope.submitted = false;
        //sets  uniqueusername and uniqueemail so form can validate on submit
        $scope.uniqueusername = true;
        $scope.uniqueemail = true;

        $scope.registerForm = function(registerForm) {
            $scope.submitted = false;
            $scope.uniqueusername = true;
            $scope.uniqueemail = true;
             
           
                if (registerForm.$valid) {
                   //continue with form processing
                    $scope.submitted = false;
                     //continue with form processing
                     alert("Form Valid: " + $scope.register.username + " " +  $scope.register.email);
                     $scope.register = {}; //reset the form
                     return; // return from function

                     //use a service to check for validity of username
                       $scope.uniqueusername = true; 
                       //use a service to check for validity of email
                       $scope.uniqueemail = true;
                    if ($scope.uniqueusername &&
                         $scope.uniqueemail ) {
                         // proceed to process form via backend service
                      }
           }
                else {
                      console.log("form is invalid");
                      $scope.submitted = true;
                    }
        
    };
})
        