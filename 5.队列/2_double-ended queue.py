# 双端队列（deque，全名double-ended queue），是一种具有队列和栈的性质的数据结构。
# 双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。双端队列可以在队列任意一端入队和出队。


class Deque():
    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list == []
    
    def add_front(self, item):
        """在队头添加元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """在队尾添加元素"""
        self.__list.append(item)

    def remove_front(self):
        """队头删除元素"""
        return self.__list.pop(0)
    
    def remove_rear(self):
        """队尾删除元素"""
        return self.__list.pop()
    
    def size(self):
        """返回队列大小"""
        return len(self.__list)
    


