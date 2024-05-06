#leetcode 977 sqaures of a sorted array
def sorted_squared(array):
    #write code here.make sure to return desired array
    squared = []
    for s in array:
        squared.append(pow(s,2))
        
    return sorted(squared)

nums = [-4,-1,0,3,10] #Input
print(sorted_squared(nums)) #Output: [0,1,9,16,100]


def sorted_squared2Pointer(array):
    #write code here.make sure to return desired array
    res = []
    left = 0
    right = len(array) - 1

    while(left <= right):
        if abs(array[left]) > abs(array[right]):
            res.append(array[left] ** 2)
            left+=1
        else:
            res.append(array[right] ** 2)
            right-=1

    #print(res)
    #res.reverse()
    #return res
    l = 0;
    r = len(res)-1
    while (l < r):
        
        temp = res[l]
        res[l] = res[r]
        res[r] = temp

        l+=1
        r-=1

    return res


a = [-4,-1,0,3,10] #Input
print("2 pointer:", sorted_squared2Pointer(a)) #Output: [0,1,9,16,100]