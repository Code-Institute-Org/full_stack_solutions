angular.module('TodoApp', ['ngRoute', 'RouteControllers', 'UserService', 'angular-storage']);

angular.module('TodoApp').config(function($routeProvider) {
	$routeProvider.when('/', {
		templateUrl: 'templates/home.html',
		controller: 'HomeController'
	})
	.when('/accounts/register', {
		templateUrl: 'templates/register.html',
		controller: 'RegisterController'
	});
});