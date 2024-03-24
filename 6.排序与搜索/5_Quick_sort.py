def Quick_sort(alist, start, end):
    if start >= end:
        return
    mid_value = alist[start]
    low = start
    high = end

    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    
    Quick_sort(alist, start, low-1)
    Quick_sort(alist, low+1, end)


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20 ]
    print(li)
    Quick_sort(li, 0, len(li)-1)
    print(li)
    print("*"*100)


