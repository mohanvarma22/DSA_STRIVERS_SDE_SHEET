#Brute force loop

'''2 pow 10 ni (2*2)pow 5
4 pow 5 ni 4 * (4 pow 4)
4 pow 4 = (4*4)2
observatioins n%2 == 0 
(x*x) pow n//2 n%2==1 ans = ans * x , n=n-1'''

def myPow(x,n):
    ans = 1
    power = abs(n)
    while power>0:
        if power % 2 == 1:
            ans *= x
            power -= 1
        else:
            x*=x
            power=power//2
    return ans if n>0 else 1.0/ans

if __name__ == "__main__":
    print(myPow(2, 10))  
    print(myPow(2, 0)) 