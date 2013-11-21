(function() {
  var route;

  route = function(pathname) {
    return console.log("About to reroute a request for " + pathname);
  };

  exports.route = route;

}).call(this);
