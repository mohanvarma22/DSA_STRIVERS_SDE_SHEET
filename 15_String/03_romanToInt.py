#roman to int and vice versa
class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        n=len(s)
        for i in range(n):
            if i<n-1 and d[s[i]]<d[s[i+1]]:
                total-=d[s[i]]
            else:
                total+=d[s[i]]
        return total
    
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
        string=""
        for val,symbol in roman:
            while num>=val:
                num=num-val
                string+=symbol
        return string