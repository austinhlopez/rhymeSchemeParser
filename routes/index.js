
/*
  GET home page.
*/

(function() {

  exports.index = function(req, res) {
    return res.render('index', {
      title: 'RapScheme'
    });
  };

}).call(this);
