'use strict'

describe 'Service: Myservice', () ->

  # load the service's module
  beforeEach module 'hackathonApp'

  # instantiate service
  Myservice = {}
  beforeEach inject (_Myservice_) ->
    Myservice = _Myservice_

  it 'should do something', () ->
    expect(!!Myservice).toBe true
