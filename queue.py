#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")


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

#the take away from this is you can
#learn how memory works and
#assigning two values to same memory
#can save time

#made on android phone

class Node:
    def __init__(self,value):
        self.next = None
        self.value = value 
        
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    #O(1)
    def enqueue(self,node):#->void
        #if no last node
        if self.last == None:
            #first and last are pointing
            #to same memory address
            self.first = node
            self.last = node
        else:
            #remember, first and last
            #are pointing to same node memory.
            #Set the next value for both
            #first and last...
            
            self.last.next = node
            #then assign the node to back
            self.last = node
            
            #this works because first has
            #the first Node saved,so when
            #back->Next is assigned it is
            #also assigned to the first.
            #so back can be changed
            #without loosing data.:D
        self.length +=1
        
    def dequeue(self):#->any
        #return first node
        #assign second node to first
        ans = self.first
        self.first = ans.next
        self.length -=1
        return ans.value
            
    def peek(self):
        print(f'first:{self.first.value}')
        
    #O(n)      
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
        
        
ll = Queue()
ll.enqueue(Node(10))
ll.enqueue(Node(20))
ll.enqueue(Node(15))
ll.showAll()
print(f"dequeued value: {ll.dequeue()}")
ll.showLength()

        

