
def power(mid,n,target):
    ans = 1
    for _ in range(1,n+1):
        ans *= mid
        if ans > target:
            return 2
    if ans == target:
        return 1
    return 0

def nthRoot(n,target):
    low=1
    high=target
    while low <= high:
        mid = (low+high)//2
        midpow=power(mid,n,target)
        if midpow == 1:
            return mid
        elif midpow == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = 4
m = 27
ans = nthRoot(n, m)
print("The answer is:", ans)
