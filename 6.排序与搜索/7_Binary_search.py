def binary_search(alist, item):
    n = len(alist)
    if n > 0:
        mid = n//2
        if alist[mid] == item:
            return mid
        elif alist[mid] > item:
            return binary_search(alist[:mid], item)
        else:
            res = binary_search(alist[mid+1:], item)
            if res != -1:
                return mid+1+res
            else:
                return -1
    else:
        return -1
    
def binary_search_1(alist, item):
    """非递归版本"""
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first+last)//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == "__main__":
    li = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_1(li, 8))
    print(binary_search(li, 32))

