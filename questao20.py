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
def setValuesInIndexes(self, indexes, elements):
  temp_pilha = Pilha()

  while not self.is_empty():
    temp_pilha.push(self.pop())

  for indice, elemento in zip(indexes, elements):
    if indice < 0 or indice >= temp_pilha.len():
      raise IndexError("Índice inválido.")

    temp_pilha.setValueInIndex(indice, elemento)

  while not temp_pilha.is_empty():
    self.push(temp_pilha.pop())


#implementação diversa utilizando pilhas:
def setValuesInIndexes_2(self, indexes, elements):
  for indice, elemento in zip(indexes, elements):
    self.pilha[indice] = elemento


#implementação elementar utilizando fila:
def setValuesInIndexes_3(fila, indexes, elements):
  for i in range(len(indexes)):
    index = indexes[i]

    fila.insert(index, elements[i])
    fila.remove(fila[index + 1])


#implementação diversa utilizando fila:
def setValuesInIndexes_4(fila, indexes, elements):
  for i in range(len(indexes)):
    index = indexes[i]

    fila[index] = elements[i]
