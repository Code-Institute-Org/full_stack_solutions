angular.module('formControllers',[])
    

    //create selectionController
    .controller('SelectionController',function($scope) {
        $scope.items = [{
            name: 'one',
            age: 30
        },
        {
            name: 'two',
            age: 27
        },
        {
            name: 'three',
            age: 50
        }];
        //create cars
        $scope.cars = ['mini','ferrari','bmw','VW'];
  
        $scope.wasSubmitted = false;
        $scope.selectedItem = $scope.items[0];

        $scope.selectedCar = $scope.cars[1];

        // for check box 
        $scope.checkboxModel = {
            fishing : true,
            golf : true,
            sailing: false,
            vote: 'down'
        };

        // for radio button
        $scope.color = {
            name: 'blue'
        };

        $scope.specialValue = {
            "id": "12345",
            "value": "green"
        };
        // checks if form is valid on submit
        $scope.submit = function() {
            if ($scope.selectionForm.$valid) {
  		        $scope.wasSubmitted = true;
                alert("selected car: " + $scope.selectedCar);
                alert("selected item: " + $scope.selectedItem.name + " " + $scope.selectedItem.age);
            } else {
  		        alert("form is invalid")
            }
        };
    })
    