#-*-coding:utf8;-*-
#qpy:3
#qpy:console



#tips: remember, in python all values
#are passed to methods by reference as
#is any other language without ptrs.

# a good aplication of Stacks is for 
#undo/redo functionality

# stack is LIFO (last in first out)


class Node:
    def __init__(self,value):
        self.next = None
        self.value = value 
        
class Stack:
    def __init__(self):
        self.first = None
        self.length = 0
    
    
    def push(self,node):#->void
        if isinstance(node,Node):
            node.next = self.first#assign 1st node as next node
            #assign node to first
            self.first = node
            #when node is set increase LL_Length
            self.length +=1
        else:
            print("error. pass a node to Stack.push(Node(value))")
        
    def pop(self):#->any
        #return first node
        #assign second node to first
            ans = self.first
            print(ans.value)
            self.first = ans.next
            self.length -=1
            return ans.value
           
        
    def showAll(self):#->void
        if self.first != None:
            #init node equal to first node
            node = self.first
            #loop through if no node value
            while(node != None):
                #show node value
                print(f'{node.value}')
                #assign node to next node
                node = node.next
        else:
            print()
            print("No values to show! \nAdd values with: \naddFront()\nor\naddEnd()")
        
    def clear():
        self.first = None
            
    def showLength(self):
     	print(f'length:{self.length}')
        



        
