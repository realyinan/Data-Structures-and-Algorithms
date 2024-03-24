# 选择排序（Selection sort）是一种简单直观的排序算法。
# 它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。


def Selection_sort(alist):
    n = len(alist)
    for j in range(0, n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[min_index], alist[j] = alist[j], alist[min_index]


if __name__ == "__main__":
    li = [23, 76, 12, 11, 53, 10, 3, 0, 8, 45]
    print(li)
    Selection_sort(li)
    print(li)
