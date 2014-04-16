#!/usr/bin/env python

import json
from jubatus.common.datum import Datum

def convert(body):
    id_, val_ = json.loads(body)
    elements = {} 
    for key, value in val_.iteritems():
        elements[key.encode("utf-8")] = value
    return id_, Datum(elements)
