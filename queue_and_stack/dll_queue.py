import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def enqueue(self, value):
    self.storage.add_to_tail()
    print(f"enqueue")
    pass
  
  def dequeue(self):
    self.storage.remove_from_head()
    print(f"dequeued")
    return item
    pass

  def len(self):
    return self.storage.length
    pass
