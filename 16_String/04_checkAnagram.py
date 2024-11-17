class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset1={}
        hashset2={}
        for i in s:
            if i in hashset1:
                hashset1[i]+=1
            else:
                hashset1[i]=1
        for i in t:
            if i in hashset2:
                hashset2[i]+=1
            else:
                hashset2[i]=1
        return hashset1==hashset2
    

        