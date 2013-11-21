'use strict'

describe 'Service: Lyriclookup', () ->

  # load the service's module
  beforeEach module 'hackathonApp'

  # instantiate service
  Lyriclookup = {}
  beforeEach inject (_Lyriclookup_) ->
    Lyriclookup = _Lyriclookup_

  it 'should do something', () ->
    expect(!!Lyriclookup).toBe true
