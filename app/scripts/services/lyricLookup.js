(function() {
  'use strict';
  angular.module('hackathonApp').factory('lyricLookup', [
    "$http", "$document", "$url", function($http, $document, $url) {
      return {
        getLyrics: function(artist, track) {
          var path, q;
          q = artist.replace(" ", "+") + "+" + track.replace(" ", "+");
          path = "/lyricLookup";
          return $http({
            method: 'POST',
            url: $url(path),
            data: {
              q: q
            }
          });
        }
      };
    }
  ]);

}).call(this);
