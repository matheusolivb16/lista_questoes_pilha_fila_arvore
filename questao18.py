class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


# pilha
class Pilha:

  def __init__(self):
    self.top = None

  def push(self, e):
    new_node = Node(e)
    new_node.next = self.top
    self.top = new_node

  def pop(self):
    if not self.top:
      return None
    data = self.top.data
    self.top = self.top.next
    return data

  def is_empty(self):
    if not self.top:
      return True
    temp = Pilha()
    while self.top:
      temp.push(self.pop())
    result = not temp.top
    while temp.top:
      self.push(temp.pop())
    return result

# fila


class Fila:

  def __init__(self):
    self.head = None
    self.tail = None

  def insert(self, e):
    new_node = Node(e)
    if not self.head:
      self.head = new_node
    else:
      self.tail.next = new_node
    self.tail = new_node

  def remove(self):
    if not self.head:
      return None
    data = self.head.data
    self.head = self.head.next
    if not self.head:
      self.tail = None
    return data

#implementação elementar utilizando pilhas:
def removeAllBySlice(self, indice_inicial, indice_final):
        elementos_removidos = []

        while indice_inicial <= indice_final:
            elemento = self.pilha.pop(indice_inicial)
            elementos_removidos.push(elemento)
            indice_final -= 1

        return elementos_removidos

#implementação diversa utilizando pilhas:
def removeAllBySlice_2(self, indice_inicial, indice_final):
        elementos_removidos = self.pilha[indice_inicial:indice_final+1]
        self.pilha = self.pilha[:indice_inicial] + self.pilha[indice_final+1:]

        return elementos_removidos
#implementação elementar utilizando fila:
def removeAllBySlice_3(fila, ii, i_f):
    for _ in range(i_f - ii + 1):
        fila.remove(fila[ii])
    
#implementação diversa utilizando fila:
def removeAllBySlice_4(fila, ii, i_f): 
    del fila[ii:i_f+1]

