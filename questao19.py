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
def setValueInIndex(self, indice, novo_valor):
        for i, elemento in enumerate(self.pilha):
            if i == indice:
                self.pilha[i] = novo_valor
                break

#implementação diversa utilizando pilhas:  
def setValueInIndex_2(self, indice, novo_valor):
        self.pilha[indice] = novo_valor

#implementação elementar utilizando fila:
def setValueInIndex_3(fila, i, e):
    fila.insert(i, e)
    fila.remove(fila[i+1])
#implementação diversa utilizando fila:
def setValueInIndex_4(fila, i, e):  
    fila[i] = e
