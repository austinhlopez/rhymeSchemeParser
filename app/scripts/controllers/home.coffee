'use strict'

angular.module('hackathonApp')
  .controller 'homeCtrl', ($scope, lyricLookup) ->
    $scope.searchForLyrics = () ->
      
      lyricLookup.getLyrics($scope.artistName, $scope.trackName)
      .then (success) ->
        console.log "success!"
        console.log success
        $scope.lyrics = success.data
        $scope.lyricsModal()
        
      , (error) ->
        console.log "shit an error!"
       console.log "whatever"

  $scope.lyricsModal = ->
    modal = $modal(
      template: $url('')
      show: true
      backdrop: 'static'
      keyboard: false
      scope: $scope.$new()
     )