"""
    Author: Dominic MacIsaac
    Course: CSCD501
    Programming Assignment #1
"""

from copy import deepcopy
import random


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


def get_digit_from_val(val, dig):
    if len(val) <= dig:
        return 0
    return int(s[len(s) - dig - 1])


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
    C = [0] * (k + 1)

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
    k = 10
    for i in range(0, d):
        B = [""] * len(A)
        count_sort_for_radix(A, B, k, i)
        A = deepcopy(B)
    return A


if __name__ == "__main__":
    A = ["CBADACCDDJGLEJZS", "abc", "ABFDSA", "18fndsaFDs"]
    print(A[5] == None)
    d = 256
    A = radix_sort(A, d)
    print(A)
