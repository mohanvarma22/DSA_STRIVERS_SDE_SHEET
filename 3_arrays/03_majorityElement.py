#hashmap approach
#optimal approach
'''Moore's Voting Algorithm
according to this algo if some element occurs more than
n//2times then the count of the element will not be cancelled out
steps to solve
apply moore's algo
verify the element
'''

def majorityElement(arr):
    element=arr[0]
    count=1
    n=len(arr)
    for i in range(1,len(arr)):
        if count==0:
            count = 1
            element=arr[i]
        elif arr[i] == element:
            count+=1
        else:
            count-=1
    count1=0
    for i in range(n):
        if arr[i] == element:
            count1+=1
    if count1>n//2:
        return element   
    else:
        return False
        

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)