'use strict'

angular.module('hackathonApp')
  .factory '$url', [
    "$window"
    ($window) ->
      (path) ->
        fullPath = $window.location.origin + path
   ]
      
      