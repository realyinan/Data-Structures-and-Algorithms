# 队列（queue）是只允许在一端进行插入操作，而在另一端进行删除操作的线性表。
# 队列是一种先进先出的（First In First Out）的线性表，简称FIFO。
# 允许插入的一端为队尾，允许删除的一端为队头。
# 队列不允许在中间部位进行操作！假设队列是q=（a1，a2，……，an），那么a1就是队头元素，而an是队尾元素。
# 这样我们就可以删除时，总是从a1开始，而插入时，总是在队列最后。这也比较符合我们通常生活中的习惯，排在第一个的优先出列，最后来的当然排在队伍最后。


class Queue():
    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list == []
    
    def enqueue(self, item):
        """进队列"""
        self.__list.append(item)

    def dequeue(self):
        """出队列"""
        return self.__list.pop(0)
    
    def size(self):
        return len(self.__list)
    

if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    print(q.size())
    print("*"*100)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.is_empty())
    print(q.size())
    print("*"*100)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())




