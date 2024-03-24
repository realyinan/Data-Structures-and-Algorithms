# 一种更复杂的链表是“双向链表”或“双面链表”。
#每个节点有两个链接：一个指向前一个节点，当此节点为第一个节点时，指向空值；而另一个指向下一个节点，当此节点为最后一个节点时，指向空值。


class Node():
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None

class doubleLinkList():
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print(" ")

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur
    
    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
    

if __name__ == "__main__":
    ll = doubleLinkList()
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