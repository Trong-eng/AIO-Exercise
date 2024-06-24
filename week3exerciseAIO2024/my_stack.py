class MyStack:
  def __init__(self, capicity):
    self.capicity = capicity
    self.stack = []
  def is_empty(self):
    return len(self.stack) == 0
  def is_full(self):
    return len(self.stack) == self.capicity
  def push(self, item):
    if self.is_full():
      raise Exception('Overflow')
    self.stack.append(item)
  def pop(self):
    if self.is_empty():
      raise Exception('Underflow')
    self.stack.pop()
  def top(self):
    if self.is_empty:
      return 'is empty'
    return self.stack[-1]