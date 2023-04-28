
"""
asteriks next to state means state is final

language: uneven amount of a's and must end with b
input:
states: a b c*
transitions:
a -> "a" -> b
a -> "b" -> a
b -> "a" -> a
b -> "b" -> c
"""

class state:
  def __init__(self, is_final):
    self.is_final = is_final

class transition:
  def __init__(self, begin, change, end):
    self.begin = begin
    self.change = change
    self.end = end

class automaton:
  """
  states:
  transitions:
  """
  def __init__(self, states, transitions):
    self.states = states
    self.transitions = transitions


  def to_regex():
    pass