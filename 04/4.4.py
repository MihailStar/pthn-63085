# 1
from math import isqrt
def is_prime(num: int) -> bool:
    """
    Простое ли?
    @tutorial https://github.com/MihailStar/pthn-100707/blob/fb6096bb99ebc5040876bac8c81d86eb9e08465d/09/9.2.py#L81
    """
    if num < 2:
        return False
    for divider in range(2, isqrt(num) + 1):
        if num % divider == 0:
            return False
    return True
print("Yes" if is_prime(int(input())) else "No")


# 2
def sum_of_divisors(num: int) -> int:
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result += i
    return result
print(sum_of_divisors(int(input())))
