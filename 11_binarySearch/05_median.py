'''brute force while lo esi two arrays ni kalpi third sorted
array create chesi andulo nunchi median kanipettali'''

#better
'''def medianTwoSorted(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    length=n+m
    ind2=length//2
    ind1=ind2-1
    count=0
    el1,el2=-1,-1
    i,j=0,0
    while i<n and j<m:
        if arr1[i]<arr2[j]:
            if count == ind1:
                el1=arr1[i]
            if count == ind2:
                el2=arr1[i]
            count+=1
            i+=1
        else:
            if count == ind1:
                el1=arr2[j]
            if count == ind2:
                el2=arr2[j]
            count+=1
            j+=1
    while i<n:
        if count == ind1:
            el1=arr1[i]
        if count == ind2:
            el2=arr1[i]
        count+=1
        i+=1
    while j<m:
        if count == ind1:
            el1=arr2[j]
        if count == ind2:
            el2=arr2[j]
        count+=1
        j+=1
    if length%2==1:
        return float(el2)
    return float(el1+el2)/2'''





if __name__ == "__main__":
    a = [1, 4, 7, 10, 12]
    b = [2, 3, 6, 15]
    print("The median of two sorted arrays is", "{:.1f}".format(medianTwoSorted(a, b)))

