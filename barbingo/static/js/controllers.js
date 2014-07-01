var barBingo = angular.module("barBingo", []);

barBingo.controller('BingoBoardCtrl', function ($scope, $http){
    $http.get('/api/v0/game/1/card/1/').success(function(data){
        $scope.squares = data.squares;
        console.log($scope);
    });
});