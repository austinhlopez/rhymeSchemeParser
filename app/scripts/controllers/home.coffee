'use strict'

angular.module('hackathonApp')
  .controller 'homeCtrl', ($scope, lyricLookup) ->
    $scope.searchForLyrics = () ->
      lyricLookup.getLyrics($scope.artistName, $scope.trackName)
      
