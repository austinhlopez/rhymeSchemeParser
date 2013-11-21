(function() {
  'use strict';
  angular.module('hackathonApp').factory('lyricLookup', [
    "$http", "$document", function($http, $document) {
      return {
        getLyrics: function(artist, track) {
          var q, url;
          q = artist.replace(" ", "+") + "+" + track.replace(" ", "+");
          url = "http://search.azlyrics.com/search.php?q=" + q + "&callback=JSON_CALLBACK";
          return $http({
            method: 'GET',
            url: url,
            headers: {
              "Content-Type": "text/html; charset=UTF-8"
            }
          });
        }
      };
    }
  ]);

}).call(this);
