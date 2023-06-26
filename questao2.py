# Pilha com lista encadeada (push com classe)
class Pilha:

  class Node:

    def __init__(self, data, next=None):
      self.data = data
      self.next = next

  def __init__(self):
    self.top = None

  def empty(self):
    return self.top is None

  def pushWithClassLinkedList(self, element):
    new_node = Pilha.Node(element)
    new_node.next = self.top
    self.top = new_node


linked_list = []


def pushWithClassLinkedList(e):
  linked_list.push(e)


# Pilha com array (push com array)
class PilhaArray:

  def __init__(self):
    self.data = []

  def empty(self):
    return len(self.data) == 0

  def pushWithArray(self, element):
    self.data.append(element)


array_list = []


def pushWithArray(e):
  array_list.append(e)


# Fila com lista encadeada (insert com classe)
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

  def insertWithClassLinkedList(self, element):
    new_node = Fila.Node(element)
    if self.empty():
      self.head = new_node
    else:
      self.tail.next = new_node
    self.tail = new_node


def insertWithClassLinkedList(e):
  linked_list.insert(e)


# Fila com array (append com array)
def insertWithArray(e):
  array_list.insert(0, e)
