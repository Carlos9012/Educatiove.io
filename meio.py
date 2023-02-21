#Ponteiros rápidos e lentos
#Meio da lista encadeada
#Given a singly linked list, return the middle node of the linked list. 
# If the number of nodes in the linked list is even, return the second middle node.
class Pilha:

  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

  def push(self, newData=None, ):
    if newData is None:
      return

    f = Pilha(newData, None)

    filaAux = self #copia
    while filaAux.next is not None:
      filaAux = filaAux.next

    filaAux.next = f
  
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

  
  def meio(self):
    aux = Pilha(self.data, self.next)
    box = []
    aux.pop()
    while True:
      f = aux.pop()
      box.append(f)
      if f is None:
        break

    box.pop(-1)
    print(box)
    janela = int(len(box)/2)
    return box[janela]
    
if __name__ == "__main__":
  
  pf = Pilha()
  pf.push('A')
  pf.push('B')
  pf.push('C')
  pf.push('D')
  pf.push('E')
  pf.push('F')
  print(pf.meio())