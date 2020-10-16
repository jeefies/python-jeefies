import os
import sys
import random


def _check_type(obj: (int, tuple, list)):
    '''
    A function to check the size type is match or not
    '''
    if isinstance(obj, int):
        return obj, int
    if isinstance(obj, (tuple, list)):
        if len(obj) > 1:
            return tuple(obj), tuple
        elif len(obj) == 1:
            return _check_type(obj[0])
        return None
    raise TypeError('The argument in must be an integer or a tuple or a list')


def matrixrand(start: int, end: int, size=None) -> tuple:
    '''
    def matrxrand(start, end, size)
    size can be a int or an int array
    A function to return a random matrix by tuple type
    :matrixrand(end, size) -> matrixrand(0, end, size)
    the return numbers include the start and the end numbers
    '''
    if not size:
        start, end, size = 0, start, end
    if isinstance(size, int):
        return tuple(random.randint(start, end) for _ in range(size))
    elif isinstance(size, (tuple, list)) and len(size) > 1:
        return tuple(matrixrand(start, end, size[1:]) for _ in range(size[0]))
    elif isinstance(size, (tuple, list)):
        return matrixrand(start, end, size[0])


def _min_sum(size):
    """
    help the randsum function to work better
    Get the number of the size(matrix)
    """
    size, tipe = _check_type(size)
    res = 1
    if tipe == int:
        return size
    else:
        for a in size:
            res *= _min_sum(a)
        return res


def randsum(sum_all: int, size) -> list:
    """
    return a list that the sum is equal to the sum_all according too the size
    !: all integers
    """
    min_sum = _min_sum(size)
    if min_sum > sum_all:
        raise OverflowError('Data overflowed')
    li = []
    for a in range(min_sum):
        li.append(random.randint(0, sum_all - min_sum - sum(li) + len(li)))
    min_index = li.index(min(li))
    li[min_index] = li[min_index] - sum(li) + sum_all
    random.shuffle(li)
    return li


if __name__ == '__main__':
    rand = matrixrand
    print(rand(7, 2))
    print(rand(1, 7, (7, 7)))
