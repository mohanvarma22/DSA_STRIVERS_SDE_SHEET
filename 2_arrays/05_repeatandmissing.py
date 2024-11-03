#using nested loops for count (brute force)
#using hashing (better)
#using maths optimal
'''to find repeating and missing we can form
2 equations and find it from there
assume 
s = sum of the array
sn = sum of n natural numbers of the array
val1 = s-sn => x - y (x is the repeating number y is the missing num)
s2 = sum of squares
s2n = sum of squares of 1st n natural numberes
val2 = s2 -s2n => x square - y square =>(x-y)(x+y)=val2
val2/(x-y) => x+y 
so from these operations we have obtained 
x-y and x+y now if we add them up
2x => 2x/2 => repeating number
if we substitute it in x + y then we will get y

'''

def findMissingandRepeating(a):
    n=len(a)
    sn=(n*(n+1))//2
    s2n=(n*(n+1) * (2*n +1))//6
    s,s2 = 0,0
    for i in range(n):
        s += a[i]
        s2 += a[i]**2

    val1 = s - sn
    val2 = s2n - s2

    val2 = val2//val1

    x = (val1 + val2)//2
    y = x - val1

    return [x,y]

a = [1, 3, 3, 4]
missing, repeating = findMissingandRepeating(a)
print(f"Missing number: {abs(missing)}, Repeating number: {abs(repeating)}")

#using XOR
'''(1^1^3^4^2^6)^(1^2^3^4^5^6)
we get 1 ^ 5 = 4 atleast one diff bit undiddi renditili
even bits unna digits anni XOR chesi odd bits unnavi anni xor
cheste rendu result  in twonumbers missing and repeating
but the problem is that we dont know which one is missing
and which one is repeating
'''

