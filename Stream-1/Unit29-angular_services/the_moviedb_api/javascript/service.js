//create service 
angular.module('movieDBServices',[]).factory('MovieListService',function($http) 
{
//  make a get request to the url to get the data 
  
    myServiceObj = {
    			name: 'Movie Service',
    			createdBy: 'Sean',
    			getList: function(url){
        				return $http.get(url);
        				}
    		}

    //return the data 
    return myServiceObj;
  });