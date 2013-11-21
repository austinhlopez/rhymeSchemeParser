# 'Express is a minimal and flexible node.js framework, providing features...'
# Express has a host of http utility methods and connect middleware...
# Express is where app.set, app.get, etc. come from. Please go to the expressjs website
# to learn more.
express = require('express')
routes = require('./routes')
http = require('http')
path = require('path')
# q is the library for promises, same as $q for angular (yesss)
q = require('q')
# I don't have a clue what querystring is but you use it to parse the body of
# a post request, apparently.

# Built into node.js, allows http requests I guess...
request = require("request")

app = express();

# all environments
app.set('port', process.env.PORT || 3000)
app.use express.favicon()
app.use express.logger('dev')
app.use express.json()
app.use express.urlencoded()
app.use express.methodOverride() 
app.use express.bodyParser() # required to get the body of a request (see scrapeLyrics)
app.use app.router
app.use express.static(path.join(__dirname, 'app'))

# development only
if 'development' == app.get('env')
  app.set('views', __dirname + '/app');
  app.use(express.static(path.join(__dirname, 'app')))
  app.use(express.errorHandler());
else
  app.set('views', __dirname + '/dist')
  app.use(express.static(path.join(__dirname, 'dist')))

app.get '/', (req, res) ->
  res.sendfile('./app/index.html')

# TODO: think about file structure, and where these sort of post requests
# should be aggregated/handled.
app.post '/lyricLookup', (req, res) ->
  q = req.body.q
  
  # we're using azlyrics for now to try to find the webpage search results.
  url = "http://search.azlyrics.com/search.php?q=#{q}"

  # Now, make a GET request to azlyrics to return the search result page.
  # Then, grab the link for the first request result and see if we can
  # get the lyrics.
  # TODO: create an editor for the lyrics to remove any bad whitespace, etc.
  # TODO: somehow, start figuring out the node.js file structure and see if
  # we can move these methods into something a little more modularizeable. Maybe a module?
  # (don't know what that is yet)
  # TODO: Handle the case when no search results are returned.
  # TODO: On client-side, add a button to allow manual search, copy/paste.
  request url, (error, response, body) ->
    if !error and response.statusCode == 200
      # Now, we need to grab the first result url and get the lyrics. Finally, we can
      # return the lyrics to the front end.

      # First, get the index of a string that's pre-identified to precede the url of
      # the first result, after all of the preceding url's on the page.
      startIndex = body.indexOf "<div class=\"sen\">"
      truncatedString = body.substring startIndex
      hrefRegex = /a href=\"http.*\"/ 
      firstResultString = truncatedString.match(hrefRegex)[0]
      firstResultStringStripFront = firstResultString.replace('a href="', '')
      firstResultStringFinal = firstResultStringStripFront.replace('"', '')

      # Now that we have the first result, we need another get get request.
      request firstResultStringFinal, (error, response, body) ->
        if !error and response.statusCode == 200
          lyricsRegex = /<!-- start of lyrics -->[\s\S]*<!-- end of lyrics -->/
          rawLyricsString = body.match(lyricsRegex)[0]
          rawLyricsStripFront = rawLyricsString.replace("<!-- start of lyrics -->\n", "")
          rawLyricsStripBack = rawLyricsStripFront.replace("\n<!-- end of lyrics -->", "")

          #TODO: Strip this goddamn html. I don't understand why this won't work...
          rawLyricsNoHtml = rawLyricsStripBack.replace(/<[\s\S]*?>/, "")

          console.log rawLyricsNoHtml
        
#app.get '/about', (req, res) ->
#  res.sendfile('./app/views/about.html')

http.createServer(app).listen app.get('port'), () ->
  console.log "fuck."
  console.log('Express server listening on port ' + app.get('port'))
  console.log(app.routes)
