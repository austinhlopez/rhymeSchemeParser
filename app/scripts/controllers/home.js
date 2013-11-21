(function() {
  'use strict';
  angular.module('hackathonApp').controller('homeCtrl', function($scope, lyricLookup) {
    return $scope.searchForLyrics = function() {
      return lyricLookup.getLyrics($scope.artistName, $scope.trackName);
    };
  });

}).call(this);
