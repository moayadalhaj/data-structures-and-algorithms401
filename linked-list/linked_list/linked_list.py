class Node:
    """
    A class for creating a node to store a value, and a pointer to the next node.
    """
    def __init__(self,value,next_=None):
        self.value=value
        self.next = next_
    
class Linked_list:
    """
    A class for creating instances of a Linked List.
    """
    def __init__(self):
        self.head=None
    
    def insert(self, value):
        """
        Insert creates a Node with the value that was passed and adds
        it to the head of the linked list shifting all other values down
        """
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next= self.head
            self.head = node
    
    def includes(self, value):
        """
        A method in linked_list class that 
        returns True or False if value is in the linked list or not
        """
        inc = False
        current = self.head
        if not current:
            return inc
        else:
            while(current.next != None):
                if current.value == value:
                    inc = True
                    break
                current = current.next
            else:
                if(current.value == value):
                    return True
            return inc

    def __str__(self):
        """
        A method in linked_list class that 
        returns a string representing all the values in the Linked List,
        """
        str_output = ''
        current = self.head
        if not current:
            return 'None'
        else:
            while not current.next == None:
                str_output = str_output + '{ ' + str(current.value) + ' } -> '
                current = current.next
            else:
                str_output += '{ ' + str(current.value) + ' } -> None'
            return str_output
    
    def append(self, value):
        """
        Adds a node of a value to the end of Linked List
        """
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def insertBefore(self,value, new_value):
        """
        method takes two arguments to add a node 
        of a new_value before node has value==value in Linked List
        """
        try:
            node = Node(new_value)
            current = self.head
            if(current.value == value):
                self.insert(new_value)
                return
            while(current.next.value != value):
                current = current.next
            a = current.next
            current.next=node
            node.next = a
        except TypeError:
            return f'please enter a proper type'
        except:
            return "No change, method exception"
    
    def insertAfter(self,value, new_value):
        """
        method takes two arguments to add a node 
        of a new_value after node has value==value in Linked List
        """
        try:
            node = Node(new_value)
            current = self.head
            while(True):
                if(current.value == value):
                    a = current.next
                    current.next = node
                    node.next = a
                    break
                current = current.next
        except:
            return "No change, method exception"

    def kthFromEnd (self,value):
        try:
            current = self.head
            allValues = []
            while(current.next != None):
                allValues.append(current.value)
                current = current.next
            else:
                allValues.append(current.value)
            allValues.reverse()
            return allValues[value]
        except:
            return 'This linked list is not long enough'
    
if __name__ == "__main__":
    ll = Linked_list()

    ll.insert(3)
    ll.insert(5)
    node=Node(3,5)
    ll.append(4)
    ll.insertAfter(5,8)
    ll.insertBefore(8,1)
    print(ll.head.value)
    print(ll.includes(5))
    print(str(ll))