(function() {
  'use strict';
  angular.module('hackathonApp').factory('$url', [
    "$window", function($window) {
      return function(path) {
        var fullPath;
        return fullPath = $window.location.origin + path;
      };
    }
  ]);

}).call(this);
