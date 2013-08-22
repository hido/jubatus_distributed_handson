# This file is auto-generated from nearest_neighbor.idl
# *** DO NOT EDIT ***


import sys
import msgpack
import common

class neighbor_result:
  @staticmethod
  def from_msgpack (arg):
    return [ (elem_arg[0], elem_arg[1])  for elem_arg in arg]

class datum:
  def __init__(self, string_values, num_values):
    self.string_values = string_values
    self.num_values = num_values

  def to_msgpack (self):
    return (
      self.string_values,
      self.num_values,
      )

  @staticmethod
  def from_msgpack (arg):
    return datum([ (elem_arg_0_[0], elem_arg_0_[1])  for elem_arg_0_ in arg[0]],
         [ (elem_arg_1_[0], elem_arg_1_[1])  for elem_arg_1_ in arg[1]])

  def __str__(self):
    gen = common.MessageStringGenerator()
    gen.open("datum")
    gen.add("string_values", self.string_values)
    gen.add("num_values", self.num_values)
    gen.close()
    return gen.to_string()

