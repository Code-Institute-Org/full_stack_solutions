angular.module('UserService', [])
	.factory('UserAPIService', function($http) {
		UserAPIService = {
			registerUser: function(url, data) {
				return $http.post(url, data);
			}
		};
		return UserAPIService;
	});