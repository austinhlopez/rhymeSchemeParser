(function() {
  var app, express, http, path, routes, user;

  express = require('express');

  routes = require('./routes');

  user = require('./routes/user');

  http = require('http');

  path = require('path');

  app = express();

  app.set('port', process.env.PORT || 3000);

  app.use(express.favicon());

  app.use(express.logger('dev'));

  app.use(express.json());

  app.use(express.urlencoded());

  app.use(express.methodOverride());

  app.use(app.router);

  app.use(express.static(path.join(__dirname, 'app')));

  if ('development' === app.get('env')) app.use(express.errorHandler());

  app.get('/', function(req, res) {
    res.sendfile('./app/index.html');
    return res.end();
  });

  app.get('/users', user.list);

  app.get('/about', function(req, res) {
    res.sendfile('./app/views/about.html');
    return res.end();
  });

  http.createServer(app).listen(app.get('port'), function() {
    return console.log('Express server listening on port ' + app.get('port'));
  });

}).call(this);
