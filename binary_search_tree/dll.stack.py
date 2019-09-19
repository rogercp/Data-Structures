import sys
from doubly_linked_list import DoublyLinkedList

class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  #I think the distinction here between queue and stack, is that stack only 
  #operates from one side of the 'list'
  def push(self, value):
    self.storage.add_to_tail(value)
  
  def pop(self):
    return self.storage.remove_from_tail()

  def len(self):
    return self.storage.length