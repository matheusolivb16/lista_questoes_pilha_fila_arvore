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
def getValuesBySlice(self, inicio, fim):
  pilha_copia = Pilha()
  valores = Pilha()

  # Copiar os elementos da pilha original para a pilha_copia
  for elemento in self.pilha:
    pilha_copia.push(elemento)

  # Extrair os valores da pilha_copia no intervalo especificado
  for _ in range(inicio):
    pilha_copia.pop()

  for _ in range(fim - inicio + 1):
    valores.push(pilha_copia.pop())

  return valores


#implementação diversa utilizando pilha
def getValuesBySlice_2(self, inicio, fim):
  valores = self.pilha[inicio:fim + 1]
  return valores


#implementação elementar utilizando fila:
def getValuesBySlice_3(fila, ii, if_):
  valores = Fila()
  if ii >= 0 and if_ >= 0 and ii <= if_ and if_ < len(fila):
    fila_copia = fila.copy()  # Cria uma cópia da fila original

    for _ in range(ii):
      fila_copia.remove(fila_copia[0])
    valores = []
    for _ in range(ii, if_ + 1):
      valores.insert(fila_copia[0])
      fila_copia.insert(fila_copia.pop(0))

    return valores
  else:
    return []


#implementação diversa utilizando fila:
def getValuesBySlice_4(fila, ii, if_):
  if ii >= 0 and if_ >= 0 and ii <= if_ and if_ < len(fila):
    return fila[ii:if_ + 1]
  else:
    return []
