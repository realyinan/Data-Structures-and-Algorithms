# 栈（stack），有些地方称为堆栈，是一种容器，可存入数据元素、访问元素、删除元素。
# 它的特点在于只能允许在容器的一端（称为栈顶端指标，英语：top）进行加入数据（英语：push）和输出数据（英语：pop）的运算。
# 没有了位置概念，保证任何时候可以访问、删除的元素都是此前最后存入的那个元素，确定了一种默认的访问顺序。
# 由于栈数据结构只允许在一端进行操作，因而按照后进先出（LIFO, Last In First Out）的原理运作。
# 栈可以用顺序表实现，也可以用链表实现。


class stack():
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新元素到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None
        
    def is_empty(self):
        return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.peek())
    print(s.size())
    print(s.is_empty())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())








