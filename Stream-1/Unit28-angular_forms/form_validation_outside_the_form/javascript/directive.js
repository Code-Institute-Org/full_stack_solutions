//create forDirective
angular.module('formDirectives',[]).directive('ngSubValid', [function() {
  	var FOCUS_CLASS = "ng-subinvalid";
  	return {
    	restrict: 'A',
    	require: 'ngModel',
    	link: function(scope, element, attrs, ctrl) {
			scope.$watch('submitted', function() {
				if (scope.submitted && ctrl.$dirty && ctrl.$invalid) {
					element.addClass(FOCUS_CLASS);
				} else {
					element.removeClass(FOCUS_CLASS);
				}		  
			});
			element.bind('focus', function(evt) {
				element.removeClass(FOCUS_CLASS);
    		}).bind('blur', function(evt) {
        		if (scope.submitted && ctrl.$dirty && ctrl.$invalid) {
        			element.addClass(FOCUS_CLASS);
        		} else {
					element.removeClass(FOCUS_CLASS);
				}
    		});
		}
    }
}]);