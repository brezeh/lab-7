#lab 7 breze howard

#Define the Node class
class Node():
    def __init__(self, value = None):
        self._value = value #store the value for the node
        self._next = None #Initialize the next pointer to None
        self._prev = None #Initialize the previous pointer to None

    #getting value of the node
    def get_value (self):
        return self._value
    
    #setting value of the node
    def set_value (self, value):
        self._value = value

    #getting next node
    def get_next (self):
        return self._next
    
    #setting next node
    def set_next (self, next):
        self._next = next

    #getting previous node
    def get_prev (self):
        return self._prev
    
    #setting previous node
    def set_prev (self, prev):
        self._prev = prev

#create individual nodes with data values
node1 = Node(10) #first node with data 10
node2 = Node(20) #second node with data 20
node3 = Node(30) #third node with data 30

#setting up the links between nodes
node1.set_next(node2)
node2.set_prev(node1)
node2.set_next(node3)
node3.set_prev(node2)

#accessing the node values
print(node1.get_value()) 
print(node2.get_value())
print(node3.get_value())

#traversing the list forward and backward
print(node1.get_next().get_value())
print(node2.get_prev().get_value()) 