def CountSort(A,B,k):
    n = len(A)
    C = [0]*(k+1)

    for i in range(n-1):
        C[A[i]] = C[A[i]] + 1

    for i in range(1,n-1):
        print(i)
        C[i] = C[i] + C[i-1]
    
    for i in range(n-1,0,-1):
        B[C[A[i]]] = A[i]
        C[A[i]] = C[A[i]] - 1
    return B

A = [1,5,3,6,9,3,5,7,2,6,8,6,6,1,4]
B = [0] * (len(A))
k = 10

CountSort(A,B,k)
print(B)
