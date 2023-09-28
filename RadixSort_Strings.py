"""
    Author: Dominic MacIsaac
    Course: CSCD501
    Programming Assignment #1
"""

from copy import deepcopy


def count_sort(A, B, k):
    n = len(A)
    C = [0] * (k + 1)

    for i in range(n):
        C[A[i]] = C[A[i]] + 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] = C[A[i]] - 1


def get_digit_from_val(s, dig):
    """
    takes a string and returns the ascii numerical value of the character at the index of dig
    Inputs:
        s (string)
        dig (int)
    Outputs:
        val (int) - 0 if dig is outside the index of string, else ASCII value of the
            character at s[dig]
    """
    if len(s) <= dig:
        return 0
    return ord(s[len(s) - dig - 1])


def count_sort_for_radix(A, B, k, d):
    """
    Count Sort implemented specifically to work with radix sort on ASCII Strings
    Inputs:
        A (Array of Strings)- unsorted array
        B (Array of Strings) - array of length A, used for returning sorted array
        k (int) - value indicating how max value of any item in A
        d (int) - value indicating which character in the string should be used for this round
                of sorting
    Outputs:
        None
    """
    n = len(A)
    C = [0] * (k + 1)  # initailize C

    for i in range(n):
        digit_val = get_digit_from_val(A[i], d)
        C[digit_val] = C[digit_val] + 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    for i in range(n - 1, -1, -1):
        digit_val = get_digit_from_val(A[i], d)
        B[C[digit_val] - 1] = A[i]
        C[digit_val] = C[digit_val] - 1


def radix_sort(A, d):
    k = 256
    for i in range(0, d):
        B = [""] * len(A)
        count_sort_for_radix(A, B, k, i)
        A = deepcopy(B)
    return A

def read_file(path):
    try:
        with open(path, 'r') as file:
            lines = file.read().splitlines()
        return lines
    except:
        return None

def write_file(path, arr):
    try:
        with open(path, 'w') as file:
            for item in arr:
                file.write(str(item) + '\n')
    except:
        pass

if __name__ == "__main__":
    input_array = read_file('input.txt')
    sorted_array = radix_sort(input_array,len(max(input_array,key=len)))
    write_file("output.txt",sorted_array)

