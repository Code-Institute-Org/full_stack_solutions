angular.module('ourServices',[])
.factory('OurPromise', function($q, $timeout) {

  var getMessages = function() {
    var deferred = $q.defer(); // set up the promise
                               // referenced by deferred.promise
    // the function inside the timeout gets executed after delay 2000ms
    $timeout(function() {
      deferred.resolve({message: 'Its a Promise'});//return results
    }, 2000);
    return deferred.promise; //return the promise object
    };   
  return { getMessages: getMessages };
});
