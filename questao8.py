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

# implementação elementar utilizando pilha:
def getValueByIndex(self, index):
        pilha_auxiliar = Pilha()
        valor = Pilha()

        # Desempilhar os elementos até encontrar o índice desejado
        for _ in range(index + 1):
            valor = self.pop()
            pilha_auxiliar.push(valor)

        # Reempilhar os elementos na pilha original
        while not pilha_auxiliar.is_empty():
            self.push(pilha_auxiliar.pop())

        return valor
# implementação diversa utilizando pilha:       
def getValueByIndex_2(self, index):
        if index < 0 or index >= len(self):
            return None
        return self.stack[index]

# implementação elementar utilizando fila:
def getValueByIndex_3(fila, index):
    fila_copia = fila.copy()  # Cria uma cópia da fila original

    elemento = None
    while len(fila_copia) > index:
        fila_copia.remove(fila_copia[0])

    if len(fila_copia) == index + 1:
        elemento = fila_copia[0]

    return elemento
# implementação diversa utilizando fila:
def getValueByIndex_4(fila, index):
    if index >= 0 and index < len(fila):
        return fila[index]
    else:
        return None