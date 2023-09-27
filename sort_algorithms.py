
def count_sort(A,B,k):
    n = len(A)
    C = [0]*(k+1)

    for i in range(n):
        C[A[i]] = C[A[i]] + 1

    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]
    
    for i in range(n-1,-1,-1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] = C[A[i]] - 1
    return B

def count_sort_for_Radix(A,B,k,d):
    n = len(A)
    C = [0]*(k+1)

    for i in range(n):
        C[A[i]] = C[A[i]] + 1

    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]
    
    for i in range(n-1,-1,-1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] = C[A[i]] - 1
    return B

def radix_sort(A):
    return None

if __name__ == "__main__":
    A = [2,5,3,0,2,3,0,3]
    B = [0] * (len(A))
    k = max(A)

    count_sort(A,B,k)
    print(B)
