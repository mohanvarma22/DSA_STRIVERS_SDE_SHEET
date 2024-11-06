'''Brute Force

def removeDuplicates(arr: List[int]) -> int:
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
    k = len(st)
    j = 0
    for x in st:
        arr[j] = x
        j += 1
    return k'''


'''Optimal

def removeDuplicates(arr: List[int]) -> int:
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1
    '''