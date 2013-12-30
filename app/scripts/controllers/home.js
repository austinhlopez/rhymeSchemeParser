(function() {
  'use strict';
  angular.module('hackathonApp').controller('homeCtrl', function($scope, lyricLookup) {
    return $scope.searchForLyrics = function() {
      lyricLookup.getLyrics($scope.artistName, $scope.trackName).then(function(success) {
        console.log("success!");
        console.log(success);
        $scope.lyrics = success.data;
        return $scope.lyricsModal();
      }, function(error) {
        return console.log("shit an error!");
      });
      return console.log("whatever");
    };
  });

  $scope.lyricsModal = function() {
    var modal;
    return modal = $modal({
      template: $url(''),
      show: true,
      backdrop: 'static',
      keyboard: false,
      scope: $scope.$new()
    });
  };

}).call(this);
