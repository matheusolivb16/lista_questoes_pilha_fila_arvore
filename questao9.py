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

# implementação elementar utilizando pilha  
def getIndexByValue(self, valor):
        pilha_auxiliar = Pilha()
        index = None
        found = False

        # Desempilhar os elementos até encontrar o valor desejado
        while not self.is_empty():
            elemento = self.pop()
            pilha_auxiliar.push(elemento)
            if elemento == valor and not found:
                index = len(self) - 1
                found = True

        # Reempilhar os elementos na pilha original
        while not pilha_auxiliar.is_empty():
            self.push(pilha_auxiliar.pop())

        return index

# implementação diversa utilizando pilha:  
def getIndexByValue_2(self, value):
        for i in range(len(self)):
            if self.stack[i] == value:
                return i
        return -1

# implementação elementar utilizando fila:
def getIndexByValue_3(fila, valor):
    fila_copia = fila.copy()  # Cria uma cópia da fila original

    index = None
    while valor in fila_copia:
        elemento = fila_copia.pop(0)
        if elemento == valor:
            index = len(fila) - len(fila_copia) - 1
            break

    return index
# implementação diversa utilizando fila:
def getIndexByValue_4(fila, valor):
    for i, elemento in enumerate(fila):
        if elemento == valor:
            return i
    return None