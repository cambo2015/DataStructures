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

#made on android phone
# enqueue is slow O(n)

class Node:
    def __init__(self,value):
        self.next = None
        self.value = value 
        
class Queue:
    def __init__(self):
        self.first = None
        self.length = 0
    
    def enqueue(self,node):#->void
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
        
    def dequeue(self):#->any
        #return first node
        #assign second node to first
            ans = self.first
            print(ans.value)
            self.first = ans.next
            self.length -=1
            return ans.value
            
    def peek(self):
        print(f'first:{self.first.value}')
            
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
ll.peek()
print(f"dequeued value: {ll.dequeue()}")
ll.showLength()

        

