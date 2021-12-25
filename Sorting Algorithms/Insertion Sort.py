

def insertion_Sort(A):
    for i in range(1, len(A)):
        k = A[i]
        j = i - 1
        while j >=0 and k < A[j]:
            A[j+1] = A[j]
            j-=1
        A[j+1] = k
    return A

A = [64, 25, 12, 22, 11]
print(insertion_Sort(A))
