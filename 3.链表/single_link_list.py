# 单向链表也叫单链表，是链表中最简单的一种形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域。
# 这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。


class Node():
    def __init__(self, item):
        self.elem = item
        self.next = None


class singleLinkList():
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
        node.next = self.__head
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
            node.next = pre.next # 核心
            pre.next = node # 核心

    def remove(self, item):
        pre = None
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next # 核心
                else:
                    pre.next = cur.next # 核心
                break
            else:
                pre = cur
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
    ll = singleLinkList()
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


