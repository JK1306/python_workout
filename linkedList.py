class Node:
    def __init__(self,value):
        self.value = value
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None

    def add(self,value):
        if self.start is None:
            self.start = Node(value)
        else:
            current=self.start
            while current.next is not None:
                current = current.next
            current.next = Node(value)
    
    def delete(self,value):
        current = self.start
        if current.value == value:
            self.start = current.next
        else:
            while current is not None:
                previous = current
                current = current.next
                if value == current.value:
                    previous.next = current.next
    
    def print_val(self):
        currentNode = self.start
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next
        

linkListObj = LinkedList()
linkListObj.add(1)
linkListObj.add(2)
linkListObj.add(3)
linkListObj.add(4)
linkListObj.add(5)
linkListObj.print_val()
linkListObj.delete(5)
print()
linkListObj.print_val()