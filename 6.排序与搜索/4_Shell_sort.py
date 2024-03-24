def Shell_sort(alist):
    n = len(alist)
    gap = n//2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

if __name__ == "__main__":
    li = [23, 76, 12, 11, 53, 10, 3, 0, 8, 45]
    print(li)
    Shell_sort(li)
    print(li)
    