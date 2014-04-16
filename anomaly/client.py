# This file is auto-generated from anomaly.idl(0.5.2-68-g68e898d) with jenerator version 0.5.2-45-gc4cfc98/master
# *** DO NOT EDIT ***


import msgpackrpc
import jubatus.common
from .types import *
from jubatus.common.types import *

class Anomaly(jubatus.common.ClientBase):
  def __init__(self, host, port, name, timeout=10):
    super(Anomaly, self).__init__(host, port, name, timeout)

  def clear_row(self, id):
    return self.jubatus_client.call("clear_row", [id], TBool(), [TString()])

  def add(self, row):
    return self.jubatus_client.call("add", [row], TUserDef(IdWithScore),
        [TDatum()])

  def update(self, id, row):
    return self.jubatus_client.call("update", [id, row], TFloat(), [TString(),
        TDatum()])

  def overwrite(self, id, row):
    return self.jubatus_client.call("overwrite", [id, row], TFloat(), [TString(
        ), TDatum()])

  def clear(self):
    return self.jubatus_client.call("clear", [], TBool(), [])

  def calc_score(self, row):
    return self.jubatus_client.call("calc_score", [row], TFloat(), [TDatum()])

  def get_all_rows(self):
    return self.jubatus_client.call("get_all_rows", [], TList(TString()), [])
