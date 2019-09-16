import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = []

  def enqueue(self, value):
    self.storage.append(value)
    print(f"enqueue")
    pass
  
  def dequeue(self):
    item = self.storage.pop(0)
    print(f"dequeued")
    return item
    pass

  def len(self):
    return len(self.storage)
    pass
