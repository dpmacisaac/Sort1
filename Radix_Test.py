import sys
sys.path.insert(0, 'Dominic_MacIsaac_1011842_prog1/')
from RadixSort_Strings import radix_sort
import random

def test_radix_empty():
    A = []
    output = radix_sort(A,0)
    assert output == []

def test_radix_one():
    A = ["ANCDQJF"]
    output = radix_sort(A,1)
    assert output == ["ANCDQJF"]

def test_radix_two():
    A = ["AAAA", "B"]
    output = radix_sort(A,len(max(A, key=len)))
    assert output == ["AAAA", "B"]

def test_radix_two_2():
    A = ["B", "AAAA"]
    output = radix_sort(A,len(max(A, key=len)))
    assert output == ["AAAA", "B"]

def test_radix_three():
    A = ["BBB", "AAA", "C"]
    output = radix_sort(A,len(max(A, key=len)))
    assert output == ["AAA", "BBB", "C"]

def test_radix_three_2():
    A = ["CCC", "BCCC", "ACCA"]
    output = radix_sort(A,len(max(A, key=len)))
    assert output == ["ACCA", "BCCC", "CCC"]

def test_radix_given():
    A = ["bcde", "abcd", "a", "efg","abcde"]
    output = radix_sort(A,len(max(A, key=len)))
    assert output == ["a", "abcd", "abcde", "bcde", "efg"]

def test_radix_long():
    A = ["bcde", "abcd", "a", "efg","abcde", "fdsaf", "zzz", "azazz", "THEE"]
    output = radix_sort(A,len(max(A, key=len)))
    assert output == ["THEE","a", "abcd", "abcde", "azazz","bcde", "efg", "fdsaf", "zzz"]