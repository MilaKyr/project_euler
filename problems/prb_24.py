"""
Lexicographic permutations

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from typing import List
from itertools import permutations


def heap_permutations(n: List[int], size: int) -> List[List[int]]:
    if size == 1:
        yield n+[]
    else:
        for hp in heap_permutations(n, size - 1):
            yield hp
        for i in range(size - 1):
            j = 0 if size % 2 else i
            n[j], n[size - 1] = n[size - 1], n[j]
            for hp in heap_permutations(n, size - 1):
                yield hp


if __name__ == "__main__":
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    hps = sorted(heap_permutations(values, len(values)))
    itertools_perms = sorted(permutations(values))
    assert hps[999999] == list(itertools_perms[999999])
    print(f"The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9"
          f"is {hps[999999]}")
