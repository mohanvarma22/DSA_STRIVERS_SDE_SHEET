#Brute force
'''
def minPlatforms(n,arr,dep):
    ans = 0
    for i in range(n):
        count=1
        for j in range(i+1,n):
            if (arr[i] >=arr[j] and arr[i]<=dep[j]) or (arr[j] >= arr[i] and arr[j] <= dep[i]):
                count+=1
        ans=max(ans,count)
    return ans
'''



#Better combine both the arrays and sort them

#optimal sort arr separately and dep and usse two pointers
def minPlatforms(n,arr,dep):
    arr.sort()
    dep.sort()
    ans = 1
    count = 1
    i = 1
    j=0
    while i<len(arr) and j< len(dep):
        if arr[i] <= dep[j]:
            count += 1
            i+=1
        else:
            count-=1
            j+=1
        ans=max(ans,count)
    return ans

if __name__ == "__main__":
    arr = [900, 945, 955, 1100, 1500, 1800]
    dep = [920, 1200, 1130, 1150, 1900, 2000]
    n = len(dep)
    print("Minimum number of Platforms required",minPlatforms(n, arr, dep))