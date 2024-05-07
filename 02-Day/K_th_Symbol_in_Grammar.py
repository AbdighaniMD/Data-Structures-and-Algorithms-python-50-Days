#779. K-th Symbol in Grammar


def kth_symbol(n, k):
    #write your code here
    curr = 0
    left, right = 1, 2**(n-1)

    for _ in range(n - 1):
        mid = (left + right) // 2
        if k <= mid:
           right = mid
        else: 
            left = mid + 1
            curr = 0 if curr else 1
        
    return curr
    
n,k = 2,2 # Input
print(kth_symbol(n,k))


def kth_symbol2(n, k):
    if n == 1:
        return 0
    length = 2 ** (n - 1) 
    mid = length //2
    if k <= mid:
        return kth_symbol2(n - 1, k)
    else:
        return int (not kth_symbol2(n - 1, k - mid))
        #return 1- kth_symbol(n - 1, k - mid)

n,k = 2,2 # Input
print(kth_symbol2(n,k))
