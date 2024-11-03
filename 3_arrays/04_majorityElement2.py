#brute force nested loop
#better hashmap
#optimal

def majorityElement2(arr):
    n=len(arr)
    el1=float('-inf')
    el2=float('-inf')
    count1=0
    count2=0
    for i in range(n):
        if count1 == 0 and arr[i]!=el2:
            count1=1
            el1=arr[i]
        elif count2==0 and arr[i]!=el1:
            count2=1
            el2=arr[i]
        elif el1==arr[i]:
            count1+=1
        elif el2==arr[i]:
            count2+=1
        else:
            count1-=1
            count2-=1
    cnt1=0
    cnt2=0
    for i in range(n):
        if arr[i]==el1:
            cnt1+=1
        elif arr[i]==el2:
            cnt2+=1
    result=[]
    if cnt1>n//3:
        result.append(el1)
    if cnt2>n//3:
        result.append(el2)
    
    return result
    
arr = [11, 33, 33, 11, 33, 11]
print(majorityElement2(arr))
