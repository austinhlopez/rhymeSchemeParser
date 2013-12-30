(function() {
  'use strict';
  describe('Service: Urlservice', function() {
    var Urlservice;
    beforeEach(module('appApp'));
    Urlservice = {};
    beforeEach(inject(function(_Urlservice_) {
      return Urlservice = _Urlservice_;
    }));
    return it('should do something', function() {
      return expect(!!Urlservice).toBe(true);
    });
  });

}).call(this);
