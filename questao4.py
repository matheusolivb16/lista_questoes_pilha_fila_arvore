# pilha
class Pilha:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.top = None

    def empty(self):
        return self.top is None

    def push(self, element):
        self.top = Pilha.Node(element, self.top)

    def pop(self):
        if not self.empty():
            temp = self.top
            self.top = self.top.next
            del temp

    def top(self):
        if not self.empty():
            return self.top.data
        else:
            raise RuntimeError("A pilha está vazia.")
        
# fila

class Fila:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def enqueue(self, element):
        new_node = Fila.Node(element)
        if self.empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.empty():
            temp = self.head
            self.head = self.head.next
            del temp

    def front(self):
        if not self.empty():
            return self.head.data
        else:
            raise RuntimeError("A fila está vazia.")
# Implementação elementar utilizando Pilhas

def peek_A(self):
  peek = self.pop()
  self.push(peek)
  return peek

# Implementação diversa utilizando Pilhas

def peek_B(self):
  return self.data

# Implementação elementar utilizando Filas
  
def first_C(self):
    first = self.remove()
  
    filaAux = Fila(first, None)
    filaAux.insert(self)

    while self.data is not None:
      self.remove()
      
    while filaAux.data is not None:
      f = filaAux.remove()
      self.insert(f)
    
    
    return first

def first_D(self):
    return self.data


  
  
  
  
  
