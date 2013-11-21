'use strict';

describe('Service: Lyriclookup', function () {

  // load the service's module
  beforeEach(module('appApp'));

  // instantiate service
  var Lyriclookup;
  beforeEach(inject(function (_Lyriclookup_) {
    Lyriclookup = _Lyriclookup_;
  }));

  it('should do something', function () {
    expect(!!Lyriclookup).toBe(true);
  });

});
