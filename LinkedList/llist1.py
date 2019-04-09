class Node:   
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:  
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end="->")
            temp = temp.next
        print()
    
       
    def insertAtBeg(self):
        data = int(input("Enter data : "))
        node = Node(data)
        if(self.head=="None"):
            self.head = node
        else:
            node.next = self.head
            self.head = node
            
    def insertAtEnd(self):
        node = Node(int(input("Enter data : ")))
        if(self.head=="None"):
            self.head = node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = node

    def insertAtPosition(self):
        node = Node(int(input("Enter data : ")))
        position = int(input("Enter Position to Insert : "))
        temp = self.head
        prev = self.head
        c = 0
        while(c<position-1):
            c+=1
            prev = temp
            temp = temp.next
        node.next=prev.next
        prev.next=node
        
    def deleteAtBeg(self):
        self.head = self.head.next
        self.printList()
        
    def deleteAtEnd(self):
        temp = self.head
        prev = temp
        while(temp.next):
            prev = temp
            temp = temp.next
        prev.next = None
        self.printList()
        
    def deleteNode(self):
        node = int(input("Enter Node to Delete : "))
        if(node == self.head.data):
            self.head = self.head.next
            self.printList()
            return
        temp = self.head
        prev = self.head
        
        while(temp.data != node):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        self.printList()
        
    def deleteAtPosition(self):
        position = int(input("Enter Position to Delete : "))
        if(position == 1):
            self.head = self.head.next
            self.printList()
            return
        temp = self.head
        prev = self.head
        c = 0
        while(c<position-1):
            c+=1
            prev = temp
            temp = temp.next
        prev.next=temp.next
        self.printList()
        
    def lengthList(self):
        temp = self.head
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        
        print("Length of List is : ",count)
        
    def searchList(self):
        node  = int(input("Enter element to Search : "))
        temp = self.head
        c = 0
        flag = 0
        while(temp):
            c+=1
            if(temp.data == node):
                flag = 1
                break
            temp = temp.next
        if(flag == 0):
            print("Element is not present in List")
        else:
            print("Element is present at position : ",c)
            
    def nthNodeBeg(self):
        position  = int(input("Enter Nth Beg Position to Search Node : "))
        if(position == 1):
            print("Element at Position 1 : ",self.head.data)
            return
        temp = self.head
        c = 0
        while(c<position-1):
            c+=1
            temp = temp.next
        print("Element at Position {0} : {1}".format(position,temp.data))
        
    def nthNodeEnd(self):
        position  = int(input("Enter Nth End Position to Search Node : "))
        temp1 = self.head
        temp2 = self.head
        while(self.head):
            c = 0
            while(c<position):
                c+=1
                temp1 = temp1.next
            while(temp1):
                temp2 = temp2.next
                temp1 = temp1.next
            print("Element at Nth End Position {0} : {1}".format(position,temp2.data))
            return
        
    def middleList(self):
        temp1 = self.head
        temp2 = self.head.next
        while(temp2 and temp2.next):
            temp1 = temp1.next
            temp2 = temp2.next.next
        print("Middle Element of List : ",temp1.data)

    def sortList(self):
        temp = self.head
        temp1 = None
        while(temp):
            if not temp1:
                #print("ist")
                temp1 = Node(temp.data)
            else:
                #print("2nd")
                node = Node(temp.data)
                temp2 = temp1
                if(temp.data>temp2.data):
                    prev = temp2
                    while(temp2.data<temp.data and temp2.next):
                        prev = temp2
                        temp2 = temp2.next
                    if not temp2.next:
                        temp2.next = node
                    else:
                        node.next = prev.next
                        prev.next = node
#                    prev.next = node
                else:
                    node.next = temp2
                    temp1 = node
            temp = temp.next
        self.head = temp1
        self.printList()
                    
        
llist = LinkedList()
llist.insertAtBeg()
llist.insertAtEnd()
llist.insertAtPosition()
llist.insertAtEnd()
llist.insertAtEnd()
llist.insertAtEnd()
llist.insertAtEnd() 

llist.printList()
llist.lengthList()

#llist.deleteAtBeg()
#llist.deleteAtEnd()
#llist.deleteNode()
#llist.deleteAtPosition()

llist.searchList()
llist.nthNodeBeg()
llist.nthNodeEnd()

llist.middleList()

llist.sortList()