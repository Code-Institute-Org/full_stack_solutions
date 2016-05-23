angular.module('routingApp', ['ngRoute', 'routingControllers']);

// configure our routes
angular.module('routingApp').config(function($routeProvider) {
	$routeProvider
		// route for the home page
		.when('/', {
			templateUrl: 'templates/home.html',
			controller: 'HomeController'
		})
		// route for the about page
		.when('/about', {
			'templateUrl': 'templates/about.html',
			'controller': 'AboutController'
		})
		// route for the contact page
		.when('/contact', {
			templateUrl: 'templates/contact.html',
			controller: 'ContactController'
		})
		.otherwise({redirectTo: '/'}); // if not above path
});