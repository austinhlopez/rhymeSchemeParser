'use strict'

angular.module('hackathonApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute'
])
  .config ['$routeProvider', ($routeProvider) ->
    $routeProvider
      .when '/',
        templateUrl: 'views/home.html'
        controller: 'homeCtrl'
      .otherwise
        redirectTo: '/'
  ]
