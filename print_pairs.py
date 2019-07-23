"""@author: Mirav Gokani
Program that prints pairs of numbers that sum up to n
for example: Given list of numbers 4, 1, 3, 5, 2, 6, 8, 7
Print pairs of numbers whose sum equals 8
>>> pairs([4, 1, 3, 5, 2, 6, 8, 7], 8)
array([[1, 7],
       [2, 6],
       [3, 5]])
"""
import numpy as np


def pairs(arr1, num):
    """Returns 2D array with pairs of numbers that sum up to num,
    else raises Exception
    """
    arr2 = []
    count = 0
    left = 0
    right = len(arr1) - 1
    arr1 = sorted(arr1)
    while left < right:
        if arr1[left] + arr1[right] > num:
            right -= 1
        elif arr1[left] + arr1[right] < num:
            left += 1
        elif arr1[left] + arr1[right] == num:
            arr2.append(arr1[left])
            arr2.append(arr1[right])
            right -= 1
            left += 1
            count += 1
    if count == 0:
        raise Exception("no pair found")
    else:
        arr2 = np.reshape(arr2, (-1, 2))  # Convert 1D to 2D array
        return arr2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    a = [20, 10, 30, 40, 50]
    result = pairs(a, 70)
    print(result)
