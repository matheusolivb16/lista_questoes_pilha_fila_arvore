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
def getAllIndexByValue(self, valor):
  pilha_auxiliar = Pilha()
  indices = Pilha()

  # Percorrer a pilha e encontrar os índices do valor desejado
  for i in range(len(self)):
    elemento = self.pop()
    pilha_auxiliar.push(elemento)
    if elemento == valor:
      indices.push(i)

  # Reempilhar os elementos na pilha original
  while not pilha_auxiliar.is_empty():
    self.push(pilha_auxiliar.pop())

  return indices


#implementação diversa utilizando pilhas:
def getAllIndexByValue_2(self, value):
  indexes = []
  for i in range(self.size()):
    if self.stack[i] == value:
      indexes.append(i)
  return indexes


# implementação elementar utilizando fila:
def getAllIndexByValue_3(fila, valor):
  fila_copia = fila.copy()  # Cria uma cópia da fila original

  indices = Fila()
  for i in range(len(fila)):
    if fila_copia[0] == valor:
      indices.insert(i)
    fila_copia.insert(fila_copia.pop(0))

  return indices


# implementação diversa utilizando fila:
def getAllIndexByValue_4(fila, valor):
  indices = []
  for i, elemento in enumerate(fila):
    if elemento == valor:
      indices.append(i)
  return indices
