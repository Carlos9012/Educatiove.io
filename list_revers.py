#Reversão no local de uma lista vinculada
#Lista de links reversos
#Given the head of a singly linked list, reverse the linked list and return its updated head.
class Pilha:

  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

  def push(self, newData=None):
    if newData is None:
      return

    p1 = Pilha(self.data, self.next)

    self.data = newData
    self.next = p1
  
  def pop(self):
    if not self:
      return None
    
    poped = self.data
    
    #if not self.next:
    if self.next is None:
      self.data = None
      self.next = None
    else:
      self.data = self.next.data
      #self.next = None
      self.next = self.next.next
    return poped

  def toArray(self, array=[]):
    if self is None:
      return

    array.append(self.data)

    if self.next is not None and self.next.data is not None:
      self.next.toArray(array)

    return array

  
  def print(self):
    array = self.toArray([])
    print(array)

  def list_revers(self):
    box = Pilha()
    while pf is not None:
      f = pf.pop()
      box.push(f)
      print(f)
      if f is None:
        break
    return box.print()


    
if __name__ == "__main__":
  
  pf = Pilha()
  pf.push('A')
  pf.push('B')
  pf.push('C')
  pf.print()
  pf.list_revers()