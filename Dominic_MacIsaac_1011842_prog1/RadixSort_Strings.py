'''
Radix Sort - Programming Assignment #1
Author: Dominic MacIsaac
Course: CSCD 501
Date: Sep 28, 2023
'''

from copy import deepcopy
import sys

def get_digit_from_val(s: str, dig: int, max_len: int) -> int:
    """
    takes a string and returns the ASCII numerical value of the character at the index of dig
    Inputs:
        s (string)
        dig (int)
        max_len (int) maximum length that a string can be
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
        max_len (int) - maximum length a string can be in the array A
    Outputs:
        None
    """
    n = len(A)

    # initialize C
    C = [0] * (k + 1) 

    # adds 1 to each index in C that corresponds to the ASCII value
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
    '''
    Radix Sort
    Inputs:
        A (array of strings)  - unsorted array
        d (int) - max amount of characters in any string in A
    Outputs:
        A (array of strings) - sorted array
    '''
    k = 256
    for i in range(0, d):
        B = [""] * len(A)
        count_sort_for_radix(A, B, k, i, d)
        A = deepcopy(B)
    return A

def read_file(path: str) -> [str] or None:
    '''
        reads file and output an array of strings
    '''
    try:
        with open(path, "r") as file:
            lines = file.read().splitlines()
        return lines
    except:
        return None

def write_file(path: str, arr: [str]) -> None:
    '''
        takes an array of strings and outputs them on newlines in a given file
    '''
    try:
        with open(path, "w") as file:
            for item in arr:
                file.write(str(item) + "\n")
    except:
        pass

if __name__ == "__main__":
    input_array = read_file(sys.argv[1]) # grabs input file
    if input_array is not None:
        sorted_array = radix_sort(input_array, len(max(input_array, key=len))) # sorts input list
        write_file("output.txt", sorted_array) # outputs sorted list
