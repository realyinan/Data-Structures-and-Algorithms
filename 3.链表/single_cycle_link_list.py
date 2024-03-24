# 单链表的一个变形是单向循环链表，链表中最后一个节点的next域不再为None，而是指向链表的头节点。


class Node():
    def __init__(self, item):
        self.elem = item
        self.next = None


class singleCycleLinkList():
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = self.__head

    def is_empty(self):
        return self.__head is None
    
    def length(self):
        if self.is_empty():
            return 0
        else:
            cur = self.__head
            count = 1
            while cur.next != self.__head:
                count += 1
                cur = cur.next
            return count
    
    def travel(self):
        if self.is_empty():
            return 
        else:
            cur = self.__head
            while cur.next != self.__head:
                print(cur.elem, end=" ")
                cur = cur.next
            print(cur.elem)

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            rear = self.__head
            while rear.next != self.__head:
                rear = rear.next
            node.next = self.__head
            self.__head = node
            rear.next = self.__head

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            rear = self.__head
            while rear.next != self.__head:
                rear = rear.next
            rear.next = node
            node.next = self.__head

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return
        else:
            pre = None
            cur = self.__head
            while cur.next != self.__head:
                if cur.elem == item:
                    if cur == self.__head:
                        rear = self.__head
                        while rear.next != self.__head:
                            rear = rear.next
                        self.__head = cur.next
                        rear.next = self.__head
                    else:
                        pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = None
                else:
                    pre.next = self.__head

    def search(self, item):
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur.next != self.__head:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next
            if cur.elem == item:
                return True
            return False
        

if __name__ == "__main__":
    ll = singleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.add(0)
    print(ll.is_empty())
    print(ll.length())
    ll.travel()
    ll.insert(-1, "a")
    ll.travel()
    ll.insert(0, "b")
    ll.travel()
    ll.insert(2, "c")
    ll.travel()
    ll.insert(9, 6)
    ll.travel()
    ll.remove("b")
    ll.travel()
    ll.remove("c")
    ll.travel()
    print(ll.length())
    print(ll.search("a"))
    print(ll.search("*"))

