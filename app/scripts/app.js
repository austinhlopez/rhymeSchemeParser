(function() {
  'use strict';
  angular.module('hackathonApp', ['ngCookies', 'ngResource', 'ngSanitize', 'ngRoute']).config([
    '$routeProvider', function($routeProvider) {
      return $routeProvider.when('/', {
        templateUrl: 'views/home.html',
        controller: 'homeCtrl'
      }).otherwise({
        redirectTo: '/'
      });
    }
  ]);

}).call(this);
