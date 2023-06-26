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
def removeAllByIndexes(self, indexes):
        elementos_removidos = []

        # Criar uma nova pilha apenas com os elementos nos índices especificados
        pilha_temporaria = Pilha()
        for i in indexes:
            if i >= 0 and i < len(self.pilha):
                elemento = self.pilha[i]
                elementos_removidos.push(elemento)
                pilha_temporaria.push(elemento)

        # Remover os elementos presentes na pilha_temporaria da pilha original
        nova_pilha = Pilha()
        while not self.is_empty():
            elemento = self.pop()
            if elemento not in pilha_temporaria.pilha:
                nova_pilha.push(elemento)

        # Atualizar a pilha original com a nova pilha resultante
        self.pilha = nova_pilha.pilha

        return elementos_removidos

#implementação diversa utilizando pilhas:
def removeAllByIndexes_2(self, indexes):
        removed_elements = []
        for index in indexes:
            if 0 <= index < self.size():
                removed_elements.append(self.stack.pop(index))
        return removed_elements

#implementação elementar utilizando fila:
def removeAllByIndexes_3(fila, indexes):
    for idx in sorted(indexes, reverse=True):
        fila.insert(idx, fila.pop(idx))
    
    for _ in range(len(indexes)):
        fila.pop()
#implementação diversa utilizando fila:
def removeAllByIndexes_(fila, indexes):
    indexes = set(indexes)  # Converte a lista de índices em um conjunto 
    nova_fila = []
    
    for idx, elemento in enumerate(fila):
        if idx not in indexes:
            nova_fila.append(elemento)
    
    fila.clear()
    fila.extend(nova_fila)