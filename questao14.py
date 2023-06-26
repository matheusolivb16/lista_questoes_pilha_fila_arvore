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
def removeByIndex(self, index):
        elemento_removido = self.pilha.pop(index)
        return elemento_removido
#implementação diversa utilizando pilha:
def removeByIndex_2(self, index):
        if 0 <= index < len(self):
            return self.stack.pop(index)
        return None
#implementação elementar utilizando fila:
def removeByIndex_3(fila, i):
    if i >= 0 and i < len(fila):
        fila.remove(i)
#implementação diversa utilizando fila:
def removeByIndex_4(fila, i):
    if i >= 0 and i < len(fila):
        fila_copia = fila.copy()  # Cria uma cópia da fila original
        fila.clear()  # Limpa a fila original
        
        for idx, elemento in enumerate(fila_copia):
            if idx != i:
                fila.append(elemento)