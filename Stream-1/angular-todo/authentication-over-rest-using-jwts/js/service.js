angular.module('UserService', [])
	.factory('UserAPIService', function($http) {
		UserAPIService = {
			callAPI: function(url, data) {
				return $http.post(url, data);
			}
		};
		return UserAPIService;
	});