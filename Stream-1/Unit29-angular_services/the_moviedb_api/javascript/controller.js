angular.module('movieDBControllers',[])
.controller('MovieListController',function($scope,MovieListService) {
// pass in url and api key for tmdb
   var url = "https://api.themoviedb.org/3/movie/upcoming?api_key=1a875f281e824935fe472da9d41f2617";
   //create array for movielist
   $scope.movieList = [];
   
   //fill movieList with data from url 
   MovieListService.getList(url).then(
      function(result){
          $scope.movieList = result.data.results;  

      }
      //in case of error retrieving  data
      ).catch(
        function(error) { 
          console.log('error', error)
        });
});
