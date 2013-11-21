(function() {
  'use strict';
  describe('Controller: HomectrlCtrl', function() {
    var HomectrlCtrl, scope;
    beforeEach(module('hackathonApp'));
    HomectrlCtrl = {};
    scope = {};
    beforeEach(inject(function($controller, $rootScope) {
      scope = $rootScope.$new();
      return HomectrlCtrl = $controller('HomectrlCtrl', {
        $scope: scope
      });
    }));
    return it('should attach a list of awesomeThings to the scope', function() {
      return expect(scope.awesomeThings.length).toBe(3);
    });
  });

}).call(this);
