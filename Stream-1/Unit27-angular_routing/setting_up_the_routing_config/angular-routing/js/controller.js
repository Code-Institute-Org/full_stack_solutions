/** add the routing controller first
then add the home, about and contact controllers
passing in the title via %scope.title */
angular.module('routingControllers', [])
	.controller('HomeController', function($scope) {
		$scope.title = "Home";
	})
	.controller('AboutController', function($scope) {
		$scope.title = "About"
	})
	.controller('ContactController', function($scope) {
		$scope.title = "Contact"
	});