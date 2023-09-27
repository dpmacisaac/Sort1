from sort_algorithms import count_sort
from sort_algorithms import radix_sort
import random

def test_blank_sort():
    A = []
    B = []
    k = 0
    count_sort(A,B,k)
    assert B == []

def test_one_sort():
    A = [0]
    B = [0]
    k = 0
    count_sort(A,B,k)
    assert B == [0]

def test_two_sort_ordered():
    A = [1,2]
    B = [0] * len(A)
    k = max(A)
    count_sort(A,B,k)
    assert B == [1,2]

def test_two_sort():
    A = [2,1]
    B = [0] * len(A)
    k = max(A)
    count_sort(A,B,k)
    assert B == [1,2]

def test_three_sort_1():
    A = [3,2,1]
    B = [0] * len(A)
    k = max(A)
    count_sort(A,B,k)
    assert B == [1,2,3]

def test_three_sort_2():
    A = [2,1,3]
    B = [0] * len(A)
    k = max(A)
    count_sort(A,B,k)
    assert B == [1,2,3]

def test_three_sort_3():
    A = [1,3,2]
    B = [0] * len(A)
    k = max(A)
    count_sort(A,B,k)
    assert B == [1,2,3]

def test_three_sort_4():
    A = [1,2,3]
    B = [0] * len(A)
    k = max(A)
    count_sort(A,B,k)
    assert B == [1,2,3]

def test_ten_sort():
    for i in range(10):
        A = [random.randint(0,10) for i in range(10)]
        B = [0] * len(A)
        k = max(A)
        count_sort(A,B,k)
        assert B == sorted(A)