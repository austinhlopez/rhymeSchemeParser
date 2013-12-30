(function() {
  'use strict';
  describe('Service: Myservice', function() {
    var Myservice;
    beforeEach(module('hackathonApp'));
    Myservice = {};
    beforeEach(inject(function(_Myservice_) {
      return Myservice = _Myservice_;
    }));
    return it('should do something', function() {
      return expect(!!Myservice).toBe(true);
    });
  });

}).call(this);
