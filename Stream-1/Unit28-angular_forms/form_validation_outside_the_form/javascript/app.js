// create the module and name it formsApp
// also include ngRoute for all our routing needs
angular.module('formsApp', ['ngRoute','formControllers','formDirectives']);
// configure our routes
angular.module('formsApp').config(function($routeProvider) {
	$routeProvider
	
		.when('/', {
			templateUrl : 'templates/registerForm.html',
			controller  : 'RegisterController'
		})
		.when("/success/:user", {
			 templateUrl : 'templates/success.html' ,
			 controller :  'successController'
		})
		.otherwise({redirectTo: '/'}); ;
});