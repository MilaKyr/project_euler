"""
Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from typing import List
from dataclasses import dataclass, field


@dataclass
class CollatzSequence:
    starting_number: int
    sequence: List[int] = field(init=False)

    def __post_init__(self):
        self.sequence = self.generate_sequence()

    def __str__(self):
        return f"Collatz Sequence with starting number of {self.starting_number}" \
               f" and sequence length of {self.len()}"

    def __gt__(self, other):
        return self.len() > other.len()

    def generate_sequence(self) -> List[int]:
        seq = [self.starting_number]
        num = self.starting_number
        while num != 1:
            num = self.update_even(num) if num % 2 == 0 else self.update_odd(num)
            seq.append(num)
        return seq

    def len(self) -> int:
        return len(self.sequence)

    @classmethod
    def update_even(cls, n: int) -> int:
        return int(n / 2)

    @classmethod
    def update_odd(cls, n: int) -> int:
        return int(3 * n + 1)


if __name__ == "__main__":
    max_collatz_seq = CollatzSequence(13)
    for starting_number in range(13, 1_000_000):
        current_seq = CollatzSequence(starting_number)
        if current_seq > max_collatz_seq:
            max_collatz_seq = current_seq
    print(f"{max_collatz_seq} produces the longest chain.")
