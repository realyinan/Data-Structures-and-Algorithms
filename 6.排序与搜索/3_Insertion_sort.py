# 插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
# 它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
# 插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。


def Insertion_sort(alist):
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break

 
if __name__ == "__main__":
    li = [23, 76, 12, 11, 53, 10, 3, 0, 8, 45]
    print(li)
    Insertion_sort(li)
    print(li)
    print("*"*100)