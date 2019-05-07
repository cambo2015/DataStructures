
#tips: remember, in python all values
#are passed to methods by reference as
#is any other language without ptrs.

#Linked Lists are the foundation
#for other data structures such as,
#stack and queue
 
class Node:
    def __init__(self,value):
        self.next = None
        self.value = value 
        
class LinkedList:
    def __init__(self):
        self.first = None
        self.length = 0
    
    #works
    def addFront(self,node):#->void
    
        node.next = self.first#assign 1st node as next node
        #assign node to first
        self.first = node
        #when node is set increase LL_Length
        self.length +=1
        
    def addEnd(self,node):#->void
        #if no first node, 
        #set first node to node seen in else statement
        if self.first != None:
            # set node to first value
            ptr = self.first
            # loop until reach last node
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = node
        else:
            self.first = node
        
    
    def showAll(self):#->void
    
        if self.first != None:
            #init node equal to first node
            node = self.first
            #loop through if no node value
            while(node != None):
                #show node value
                print(node.value)
                #assign node to next node
                node = node.next
        else:
            print()
            print("No values to show! \nAdd values with: \naddFront()\nor\naddEnd()")
        
        
ll = LinkedList()
ll.addFront(Node(10))
ll.addEnd(Node(20))
ll.addFront(Node(15))
ll.showAll()
        
