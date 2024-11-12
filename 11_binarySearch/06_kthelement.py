'''brute force

            def kthElement(a, b, m, n, k):
                arr3 = []
            
                # Apply the merge step:
                i, j = 0, 0
                while i < m and j < n:
                    if a[i] < b[j]:
                        arr3.append(a[i])
                        i += 1
                    else:
                        arr3.append(b[j])
                        j += 1
            
                # Copy the left-out elements:
                arr3.extend(a[i:])
                arr3.extend(b[j:])
                return arr3[k - 1]
        
            
        
        '''

#better code lo we can keep a counter and aa el store cheskuni return cheyyadame


if __name__ == "__main__":
                a = [2, 3, 6, 7, 9]
                b = [1, 4, 8, 10]
                print("The k-th element of two sorted arrays is:", kthElement(a, b, len(a), len(b), 5))