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
def removeAllByValue(self, valor):
        elementos_removidos = []
        pilha_temporaria = []

        # Enquanto a pilha não estiver vazia, desempilhar e verificar cada elemento
        while not self.is_empty():
            elemento = self.pop()

            if elemento == valor:
                elementos_removidos.push(elemento)
            else:
                pilha_temporaria.push(elemento)

        # Reinserir os elementos não removidos de volta na pilha original
        while pilha_temporaria:
            self.push(pilha_temporaria.pop())

        return elementos_removidos

#implementação diversa utilizando pilhas:
def removeAllByValue_2(self, value):
        removed_elements = []
        i = 0
        while i < len(self):
            if self.stack[i] == value:
                removed_elements.append(self.stack.pop(i))
            else:
                i += 1
        return removed_elements

#implementação elementar utilizando fila:
def removeAllByValue_3(fila, e):
    while e in fila:
        fila.remove(e)
#implementação diversa utilizando fila:
def removeAllByValue_4(fila, e):
    while e in fila:
        index = fila.index(e)
        fila_copia = fila.copy()  # Cria uma cópia da fila original
        fila.clear()  # Limpa a fila original
        
        for idx, elemento in enumerate(fila_copia):
            if idx != index:
                fila.append(elemento)
