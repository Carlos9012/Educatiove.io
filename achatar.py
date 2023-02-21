#Primeira Pesquisa da Profundidade da Árvore
#Achatar árvore binária para lista encadeada
class Lista:
  def __init__(self,data = None, next = None):
        self.next = next
        self.data = data
    
  def push(self, newData=None):
        if newData is None:
            return

        p1 = Lista(self.data, self.next)

        self.data = newData
        self.next = p1
    

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

class NodoArvore: 

  
  def __init__(self, key, dir, esq, box = []):
    self.item = key
    self.dir = dir
    self.esq = esq
    self.box = box

  
  def printTree(self, level=0):
    if self == None:
      return

    if self.dir is not None:
      self.dir.printTree(level + 1)

    print((' ' * 4 * level) + '-> ' + self.item)
    
    if self.esq is not None:
      self.esq.printTree(level + 1)
    return
    
  
  def preOrder(self, atual, box = []):
    if atual != None:
        self.box.append(atual.item)
        self.preOrder(atual.esq)
        self.preOrder(atual.dir)
    return self.box

def achatar(self = None):
    pf = Lista()

    for i in reversed(A.preOrder(A)):
        pf.push(i)
    pf.print()
    return

if __name__ == "__main__":
  G = NodoArvore('G', None, None)
  F = NodoArvore('F', None, None)
  E = NodoArvore('E', None, None)
  D = NodoArvore('D', None, None)
  
  C = NodoArvore('C', F, G)
  B = NodoArvore('B', D, E)

  A = NodoArvore('A', C, B)
  A.printTree()
  pf = Lista()
  achatar()
  
  
