#896. Monotonic Array

def monotonic_array(nums):
    #write code here
    return monotone_increasing(nums) or monotone_decreasing(nums)


def monotone_increasing(nums):
    left = 0
    right = 1
    while right < len(nums):
        if nums[left] > nums[right]:
            return False
        else: 
            left+=1
            right+=1
    return True

def monotone_decreasing(nums):
    left = 0
    right = 1
    while right < len(nums):
        if nums[left] < nums[right]:
            return False
        else: 
            left+=1
            right+=1
    return True



nums = [1,2,2,3] #Input: 
print(monotonic_array(nums)) #True
print(" ")
nums1 = [6,5,4,4]
print(monotonic_array(nums1)) #True
print(" ")
nums2 = [1,3,2]
print(monotonic_array(nums2)) #True


print("----------------------------------------------")
def monotonic_arrayOnePass(nums):
    #write code here
    increase, decrease = True, True

    for i in range(len(nums)-1):
        if not (nums[i] <= nums[i+1]):
            increase = False
        if not (nums[i] >= nums[i+1]):
            decrease = False

    return increase or decrease


nums = [1,2,2,3] #Input: 
print(monotonic_arrayOnePass(nums)) #True
print(" ")
nums1 = [6,5,4,4]
print(monotonic_arrayOnePass(nums1)) #True
print(" ")
nums2 = [1,3,2]
print(monotonic_arrayOnePass(nums2)) #True
