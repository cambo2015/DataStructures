#[author:cambo2015]
#[CC zero lsc]

#tips: remember, in python all values
#are passed to methods by reference as
#is any other language without ptrs.


#[error?]
#if you get an error it may be
#the use of f strings. 
#Just remove them to fix error
#they are a new feture in python

#made on android phone

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
        #set first node to node. See else statement
        if self.first != None:
            # set node to first value
            ptr = self.first
            # loop until reach last node
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = node
        else:
            self.first = node
        #increase length by 1
        self.length +=1
        
    
    def showAll(self):#->void
        if self.first != None:
            #init node equal to first node
            node = self.first
            #loop through if no node value
            while(node != None):
                #show node value
                print(f'value:{node.value}')
                #assign node to next node
                node = node.next
        else:
            print()
            print("No values to show! \nAdd values with: \naddFront()\nor\naddEnd()")
    def showLength(self):
     	print(f'length:{self.length}')
        
        
ll = LinkedList()
ll.addFront(Node(10))
ll.addEnd(Node(20))
ll.addFront(Node(15))
ll.showAll()
ll.showLength()

        
