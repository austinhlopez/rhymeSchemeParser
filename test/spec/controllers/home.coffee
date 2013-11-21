'use strict'

describe 'Controller: HomectrlCtrl', () ->

  # load the controller's module
  beforeEach module 'hackathonApp'

  HomectrlCtrl = {}
  scope = {}

  # Initialize the controller and a mock scope
  beforeEach inject ($controller, $rootScope) ->
    scope = $rootScope.$new()
    HomectrlCtrl = $controller 'HomectrlCtrl', {
      $scope: scope
    }

  it 'should attach a list of awesomeThings to the scope', () ->
    expect(scope.awesomeThings.length).toBe 3
