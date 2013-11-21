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


        # TODO: Write a url service that populates the url with the dev setup or the production
        # setup, depending on whether the app is run in localhost or on the server.
        $http
          method: 'POST'
          url: "http://localhost:3000/lyricLookup"
          data:
            q: q
      
    ]
    
    
