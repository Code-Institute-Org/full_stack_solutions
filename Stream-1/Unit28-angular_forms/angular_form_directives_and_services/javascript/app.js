// create the module and name it formsApp
// also include ngRoute for all our routing needs
// and add the formDirectives
angular.module('formsApp', ['ngRoute','formControllers','formDirectives']);
// configure our routes
angular.module('formsApp').config(function($routeProvider) {
	$routeProvider
	
		.when('/', {
			templateUrl : 'templates/registerForm.html',
			controller  : 'RegisterController'
		})
		

		.otherwise({redirectTo: '/'}); ;
});