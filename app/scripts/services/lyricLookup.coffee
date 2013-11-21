'use strict'

angular.module('hackathonApp')
  .factory 'lyricLookup', [
    "$http"
    "$document"
    ($http, $document) ->

      # I'm sending this thing the wrong way.
      # Get it into the backend!
      getLyrics: (artist, track) ->
        # Combine artist and track into a single query string.
        q = artist.replace(" ", "+") + "+" + track.replace(" ", "+")

        url = "http://search.azlyrics.com/search.php?q=#{q}&callback=JSON_CALLBACK"

        $http
          method: 'GET'
          url: url
          headers:
            "Content-Type": "text/html; charset=UTF-8"
            
        #.success (data) ->
        #  console.log "what the fuck."
        #console.log("whatever.")
      
    ]
    
    
