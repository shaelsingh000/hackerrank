class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
    
class linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,temp.next,sep="\t")
            temp = temp.next

    def insert_at_beginning(self,data):
        x = node(data)
        x.next= self.head
        self.head = x

    def insert_after_node(self,prev, data):
        if prev is None:
            print("Node not Present")
            return 
        else:
            new_node = node(data)
            new_node.next = prev.next
            prev.next = new_node

    def insert_after_end(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self,data):
        temp = self.head
        if (temp is not None):
            if (temp.data == data):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        if(temp == None):
                return
        prev.next = temp.next
        temp = None
    def delete_by_position(self,pos):
        c=0
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        next = temp.next.next
        temp.next = None
        temp.next = next
    def delete_list(self):
        temp = self.head
        while temp:
            prev = temp.next
            del temp.data
            temp = prev
    def length(self):
        temp = self.head
        len= 0

        while temp:
            len+=1
            temp= temp.next
        print(len)

    def searching(self,data):
        temp = self.head
        c = 0
        while temp:
            c+=1
            if (temp.data == data):
                print(data," is present at position:",c,sep="\t")
            temp = temp.next






if __name__=='__main__':
    llist = linkedlist()
    llist.head = node(1)
    second = node(2)
    third = node(3)

    llist.head.next = second
    second.next = third
    third.next = None

    llist.insert_at_beginning(4)
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(9)
    llist.insert_at_beginning(1)
    llist.insert_after_node(llist.head,6)
    llist.insert_after_node(llist.head.next.next,7)
    llist.insert_after_end(8)
    llist.delete(5)
    llist.delete_by_position(3)
    llist.length()
    llist.searching(6)
    llist.print_list()
    
   
    
