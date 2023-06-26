class LinkedList:
    def __init__(self):
        self.head = None

    def popWithClassLinkedLis(self, e):
        if self.head is None:
            return None

        if self.head.data == e:
            popped_element = self.head.data
            self.head = self.head.next
            return popped_element

        current = self.head
        while current.next:
            if current.next.data == e:
                popped_element = current.next.data
                current.next = current.next.next
                return popped_element
            current = current.next

        return None

    def removeWithClassLinkedLis(self, e):
        if self.head is None:
            return None

        if self.head.data == e:
            removed_element = self.head.data
            self.head = self.head.next
            return removed_element

        previous = None
        current = self.head
        while current:
            if current.data == e:
                removed_element = current.data
                previous.next = current.next
                return removed_element
            previous = current
            current = current.next

        return None


def popWithArray(arr, e):
    if e in arr:
        arr.remove(e)
        return e
    return None

def popWithArray(arr):
        
        arr.remove(0)
      
    return None

def removeWithArray(arr, e):
    if e in arr:
        arr.remove(e)
        return e
    return None