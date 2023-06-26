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


#implementação elementar utilizando pilha
def getValuesByIndexes(self, indexes):
  pilha_auxiliar = Pilha()
  valores = Pilha()

  # Percorrer a pilha e obter os valores nos índices especificados
  for i in range(self.size()):
    elemento = self.pop()
    pilha_auxiliar.push(elemento)
    if i in indexes:
      valores.push(elemento)

  # Reempilhar os elementos na pilha original
  while not pilha_auxiliar.is_empty():
    self.push(pilha_auxiliar.pop())

  return valores


#implementação diversa utilizando pilha
def getValuesByIndexes_2(self, indexes):
  values = []
  for index in indexes:
    if 0 <= index < self.size():
      values.append(self.stack[index])
    else:
      values.append(None)
  return values


#implementação elementar utilizando fila:
def getValuesByIndexes_3(fila, indexes):
  valores = Fila()
  fila_copia = fila.copy()  # Cria uma cópia da fila original

  for i in indexes:
    if i >= 0 and i < len(fila_copia):
      for _ in range(i):
        fila_copia.insert(fila_copia.pop(0))
      valores.insert(fila_copia[0])

  return valores


#implementação diversa utilizando fila:
def getValuesByIndexes_4(fila, indexes):
  valores = []
  for i in indexes:
    if i >= 0 and i < len(fila):
      valores.append(fila[i])
  return valores
