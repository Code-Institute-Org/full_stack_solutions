
//create the angular promiseController
angular.module('promiseControllers',[])
.controller('PromiseController', function($scope, OurPromise) {
    $scope.PromiseComplete = false;
    OurPromise.getMessages().then(function(result) {
               //messages is what is returned from resolve()
               $scope.message = result.message;
        	   $scope.PromiseComplete = true;
    });
});