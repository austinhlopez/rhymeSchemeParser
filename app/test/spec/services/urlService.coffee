'use strict'

describe 'Service: Urlservice', () ->

  # load the service's module
  beforeEach module 'appApp'

  # instantiate service
  Urlservice = {}
  beforeEach inject (_Urlservice_) ->
    Urlservice = _Urlservice_

  it 'should do something', () ->
    expect(!!Urlservice).toBe true
