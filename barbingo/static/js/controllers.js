var barBingo = angular.module("barBingo", []);

barBingo.controller('BingoBoardCtrl', function ($scope, $http){
    $http.get('/api/v0/game/1/card/1/').success(function(data){
        $scope.squares = data.squares;
        console.log($scope.squares);
    });

    $scope.clickSquare = function(clickEvent) {
        console.log(clickEvent);
        $http({
            url: '/api/v0/game/1/card/1/',
            method: "POST",
            data: {action: "promote", square: clickEvent},
            headers: {'Content-Type': 'application/json'}
        }).success(function (data) {
            $scope.squares[data.square.position].status = data.square.status
        })
    };

    $scope.updateSquare = function(data) {
        console.log("WOOT")
        square = data.square;
        console.log("MYSQUARE")
        console.log(square);
        $scope[square.position] = square;
    };
});