# This file is auto-generated from anomaly.idl(0.5.2-68-g68e898d) with jenerator version 0.5.2-45-gc4cfc98/master
# *** DO NOT EDIT ***


import sys
import msgpack
import jubatus.common
from jubatus.common.types import *

class IdWithScore:
  TYPE = TTuple(TString(), TFloat())

  def __init__(self, id, score):
    self.id = id
    self.score = score

  def to_msgpack(self):
    t = (self.id, self.score)
    return self.__class__.TYPE.to_msgpack(t)

  @classmethod
  def from_msgpack(cls, arg):
    val = cls.TYPE.from_msgpack(arg)
    return IdWithScore(*val)

  def __repr__(self):
    gen = jubatus.common.MessageStringGenerator()
    gen.open("id_with_score")
    gen.add("id", self.id)
    gen.add("score", self.score)
    gen.close()
    return gen.to_string()

