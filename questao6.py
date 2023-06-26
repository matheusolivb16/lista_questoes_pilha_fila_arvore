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

#Implementação elementar utilizando Pilhas:
def count_elements(self):
        temp_pilha = Pilha()
        count = 0

        while not self.is_empty():
            temp_pilha.push(self.pop())
            count += 1

        while not temp_pilha.is_empty():
            self.push(temp_pilha.pop())

        return count
#Implementação diversa utilizando Pilhas:
def count_elements_2(string):
  stack = []
  for character in string:
    stack.append(character)
  count = 0
  while len(stack) > 0:
    stack.pop()
    count += 1
    print(count)

# Implementação elementar utilizando Filas:
def obter_tamanho_fila(fila):
    fila_copia = fila.copy()  # Cria uma cópia da fila original

    tamanho = 0
    while fila_copia:
        fila_copia.remove(fila_copia[0])
        tamanho += 1

    return tamanho

# Implementação diversa utilizando Filas:
def count_elements_4(string):
  queue = []
  for character in string:
    queue.insert(0, character)
  count = 0
  while len(queue) > 0:
    queue.remove(queue[-1])
    count += 1
    print(count)
