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
    
    def is_empty(self):
        return self.head is None

# Implementação elementar utilizando Pilhas
def is_empty(pilha):
    # Tenta remover um elemento da pilha
    try:
        pilha.pop()
    except IndexError:
        # Se ocorrer um IndexError, a pilha está vazia
        return True
    else:
        # Se nenhum IndexError ocorrer, a pilha não está vazia
        return False
    
pilha = []
print(is_empty(pilha)) 

pilha.append(1)
print(is_empty(pilha)) 

# Implementação diversa utilizando Pilhas:
from collections import deque

def is_empty(data_structure):
    stack = deque(data_structure)
    print(bool(stack))

is_empty([])


# Implementação elementar utilizando Filas:
def is_empty(fila):
    # Tenta remover um elemento da fila
    try:
        fila.remove(fila[0])
    except IndexError:
        # Se ocorrer um IndexError, a fila está vazia
        return True
    else:
        # Se nenhum IndexError ocorrer, a fila não está vazia
        return False
    
fila = [1, 2, 3]
print(is_empty(fila))

# Implementação diversa utilizando Pilhas:
from queue import Queue

def is_empty(data_structure):
    queue = Queue()
    for item in data_structure:
        queue.put(item)
    print(queue.empty())

is_empty("abc")    