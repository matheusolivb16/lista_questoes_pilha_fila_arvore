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

#implementação elementar utilizando pilhas:
def last_element(self):
        temp_pilha = Pilha()

        while not self.is_empty():
            elemento = self.pop()
            temp_pilha.push(elemento)

        last_element = temp_pilha.peek()

        while not temp_pilha.is_empty():
            self.push(temp_pilha.pop())

        return last_element

#Implementação diversa utilizando Pilhas:
def last_element_2(stack):
    print(stack[-1])

# Implementação elementar utilizando Filas:
def last_element_3(fila):
    fila_copia = fila.copy()  # Cria uma cópia da fila original

    while len(fila_copia) > 1:
        fila_copia.insert(0, fila_copia.pop())

    if fila_copia:
        ultimo_elemento = fila_copia[0]
        return ultimo_elemento
    else:
        return None
# Implementação diversa utilizando Filas:
def last_element_4(fila):
    if fila:
        ultimo_elemento = fila[-1]
        return ultimo_elemento
