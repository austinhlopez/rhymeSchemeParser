(function() {
  'use strict';
  describe('Service: Lyriclookup', function() {
    var Lyriclookup;
    beforeEach(module('hackathonApp'));
    Lyriclookup = {};
    beforeEach(inject(function(_Lyriclookup_) {
      return Lyriclookup = _Lyriclookup_;
    }));
    return it('should do something', function() {
      return expect(!!Lyriclookup).toBe(true);
    });
  });

}).call(this);
