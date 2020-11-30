# Fibbonaci
# Provide a number and we'll calculate the fibbonaci number at that point in the sequence.

from typing import List


def fibbonaci(n: int) -> int:
    if n <= 1: 
        return n
    else:
        return (fibbonaci(n-2) + fibbonaci(n-1))

# Provide a number and we'll provide a list of the the fibbonaci sequence up to that point in the sequence.
# def fibbonaci_list(n: int) -> List[int]:
#     arr = []
#     for i in range(n):
#         arr.append(fibbonaci(i))
    
#     return arr

print(fibbonaci(10))
# print(fibbonaci_list(15))