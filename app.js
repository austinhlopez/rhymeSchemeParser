(function() {
  var app, express, http, path, q, request, routes;

  express = require('express');

  routes = require('./routes');

  http = require('http');

  path = require('path');

  q = require('q');

  request = require("request");

  app = express();

  app.set('port', process.env.PORT || 3000);

  app.use(express.favicon());

  app.use(express.logger('dev'));

  app.use(express.json());

  app.use(express.urlencoded());

  app.use(express.methodOverride());

  app.use(express.bodyParser());

  app.use(app.router);

  app.use(express.static(path.join(__dirname, 'app')));

  if ('development' === app.get('env')) {
    app.set('views', __dirname + '/app');
    app.use(express.static(path.join(__dirname, 'app')));
    app.use(express.errorHandler());
  } else {
    app.set('views', __dirname + '/dist');
    app.use(express.static(path.join(__dirname, 'dist')));
  }

  app.get('/', function(req, res) {
    return res.sendfile('./app/index.html');
  });

  app.post('/lyricLookup', function(req, res) {
    var url;
    q = req.body.q;
    url = "http://search.azlyrics.com/search.php?q=" + q;
    return request(url, function(error, response, body) {
      var firstResultString, firstResultStringFinal, firstResultStringStripFront, hrefRegex, startIndex, truncatedString;
      if (!error && response.statusCode === 200) {
        startIndex = body.indexOf("<div class=\"sen\">");
        truncatedString = body.substring(startIndex);
        hrefRegex = /a href=\"http.*\"/;
        firstResultString = truncatedString.match(hrefRegex)[0];
        firstResultStringStripFront = firstResultString.replace('a href="', '');
        firstResultStringFinal = firstResultStringStripFront.replace('"', '');
        return request(firstResultStringFinal, function(error, response, body) {
          var lyricsRegex, rawLyricsNoHtml, rawLyricsString, rawLyricsStripBack, rawLyricsStripFront;
          if (!error && response.statusCode === 200) {
            lyricsRegex = /<!-- start of lyrics -->[\s\S]*<!-- end of lyrics -->/;
            rawLyricsString = body.match(lyricsRegex)[0];
            rawLyricsStripFront = rawLyricsString.replace("<!-- start of lyrics -->\n", "");
            rawLyricsStripBack = rawLyricsStripFront.replace("\n<!-- end of lyrics -->", "");
            rawLyricsNoHtml = rawLyricsStripBack.replace(/<[\s\S]*?>/, "");
            return console.log(rawLyricsNoHtml);
          }
        });
      }
    });
  });

  http.createServer(app).listen(app.get('port'), function() {
    console.log("fuck.");
    console.log('Express server listening on port ' + app.get('port'));
    return console.log(app.routes);
  });

}).call(this);
