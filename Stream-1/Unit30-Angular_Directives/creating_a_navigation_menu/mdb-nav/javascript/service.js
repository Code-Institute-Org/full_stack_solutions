angular.module('movieDBServices',[]).factory('MovieListService',function($http) {
//   
    return  { getList: getList };

    function getList(url){
			return $http.get(url);
        };
});