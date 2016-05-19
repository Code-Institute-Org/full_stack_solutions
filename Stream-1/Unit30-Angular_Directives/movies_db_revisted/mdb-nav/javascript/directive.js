angular.module('movieDBDirectives',[]).directive('movieInfoBox', function() {
  return {
    restrict: 'E',    // usage of the directive: E -> element
    scope: {
      movie: '=info'    // 'movie' set with the 'info' attribute
    },
    templateUrl: 'templates/directives/movie-info-box.html'
  };
});