// create the module and name it formsApp
// also include ngRoute for all our routing needs and include the formDirectives
angular.module('formsApp', ['ngRoute','formControllers','formDirectives']);
// configure our routes
angular.module('formsApp').config(function($routeProvider) {
	$routeProvider
	
		
		.when('/', {
			templateUrl : 'templates/selectionForm.html',
			controller  : 'SelectionController'
		})
		
		.otherwise({redirectTo: '/'}); ;
});