from Sort1.RadixSort_Strings import count_sort
from Sort1.RadixSort_Strings import radix_sort
import random
########## Count Sort ##########
def test_blank_countsort():
    A = []
    B = []
    k = 0
    count_sort(A,B,k)
    assert B == []

def test_one_countsort():
    A = [0]
    B = [0]
    k = 0
    count_sort(A,B,k)
    assert B == [0]

def test_two_countsort_ordered():
    A = [1,2]
    B = [0] * len(A)
    k = max(A)
    count_sort(A,B,k)
    assert B == [1,2]

def test_two_countsort():
    A = [2,1]
    B = [0] * len(A)
    k = max(A)
    count_sort(A,B,k)
    assert B == [1,2]

def test_three_countsort_1():
    A = [3,2,1]
    B = [0] * len(A)
    k = max(A)
    count_sort(A,B,k)
    assert B == [1,2,3]

def test_three_countsort_2():
    A = [2,1,3]
    B = [0] * len(A)
    k = max(A)
    count_sort(A,B,k)
    assert B == [1,2,3]

def test_three_countsort_3():
    A = [1,3,2]
    B = [0] * len(A)
    k = max(A)
    count_sort(A,B,k)
    assert B == [1,2,3]

def test_three_countsort_4():
    A = [1,2,3]
    B = [0] * len(A)
    k = max(A)
    count_sort(A,B,k)
    assert B == [1,2,3]

def test_ten_countsort():
    for _ in range(10):
        A = [random.randint(0,10) for i in range(10)]
        B = [0] * len(A)
        k = max(A)
        count_sort(A,B,k)
        assert B == sorted(A)

########## Radix Sort ##########

def test_blank_radixsort():
    A = []
    d = 0
    radix_sort(A,d)
    assert A == []

def test_random_radixsort():
    for i in range(1000):
        x = random.randint(0,1000)
        A = [random.randint(0,100000) for i in range(x)]
        d = 6
        D = radix_sort(A,d)
        assert D == sorted(A)