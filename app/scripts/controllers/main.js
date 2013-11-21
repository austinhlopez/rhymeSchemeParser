(function() {
  'use strict';
  angular.module('hackathonApp').controller('MainCtrl', [
    '$scope', function($scope) {
      return $scope.awesomeThings = ['HTML5 Boilerplate', 'AngularJS', 'Karma'];
    }
  ]);

}).call(this);
