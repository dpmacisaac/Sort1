from copy import deepcopy
import sys

def count_sort(A: [int], B: [int], k: int) -> None:
    n = len(A)
    C = [0] * (k + 1)

    for i in range(n):
        C[A[i]] = C[A[i]] + 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] = C[A[i]] - 1

def get_digit_from_val(s: str, dig: int, max_len: int) -> int:
    """
    takes a string and returns the ASCII numerical value of the character at the index of dig
    Inputs:
        s (string)
        dig (int)
    Outputs:
        val (int) - 0 if dig is outside the index of the string, else the ASCII value of the
            character at s[dig]
    """
    if len(s)+dig < max_len:
        return 0
    return ord(s[max_len - dig - 1])

def count_sort_for_radix(A: [str], B: [str], k: int, d: int, max_len:int) -> None:
    """
    Count Sort implemented specifically to work with radix sort on ASCII Strings
    Inputs:
        A (List of Strings) - unsorted array
        B (List of Strings) - array of length A, used for returning the sorted array
        k (int) - value indicating the maximum value of any item in A
        d (int) - value indicating which character in the string should be used for this round
                of sorting
    Outputs:
        None
    """
    n = len(A)
    C = [0] * (k + 1)  # initialize C

    for i in range(n):
        digit_val = get_digit_from_val(A[i], d, max_len)
        C[digit_val] = C[digit_val] + 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    for i in range(n - 1, -1, -1):
        digit_val = get_digit_from_val(A[i], d, max_len)
        B[C[digit_val] - 1] = A[i]
        C[digit_val] = C[digit_val] - 1

def radix_sort(A: [str], d: int) -> [str]:
    k = 256
    for i in range(0, d):
        B = [""] * len(A)
        count_sort_for_radix(A, B, k, i, d)
        A = deepcopy(B)
    return A

def read_file(path: str) -> [str] or None:
    try:
        with open(path, "r") as file:
            lines = file.read().splitlines()
        return lines
    except:
        return None

def write_file(path: str, arr: [str]) -> None:
    try:
        with open(path, "w") as file:
            for item in arr:
                file.write(str(item) + "\n")
    except:
        pass

if __name__ == "__main__":
    input_array = read_file(sys.argv[1])
    if input_array is not None:
        sorted_array = radix_sort(input_array, len(max(input_array, key=len)))
        write_file("output.txt", sorted_array)
