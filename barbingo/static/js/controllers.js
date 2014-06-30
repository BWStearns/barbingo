var barBingo = angular.module("barBingo", []);

barBingo.controller('BingoBoardCtrl', function ($scope){
    $scope.squares = [
    {'text': "Hi there", "pos": 1},
    {'text': "Yo there", "pos": 2},
    {'text': "Hi Yo", "pos": 3}
    ];
    
});