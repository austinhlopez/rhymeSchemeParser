(function() {
  'use strict';
  angular.module('hackathonApp').factory('lyricLookup', [
    "$http", "$document", function($http, $document) {
      return {
        getLyrics: function(artist, track) {
          var q;
          q = artist.replace(" ", "+") + "+" + track.replace(" ", "+");
          return $http({
            method: 'POST',
            url: "http://localhost:3000/lyricLookup",
            data: {
              q: q
            }
          });
        }
      };
    }
  ]);

}).call(this);
