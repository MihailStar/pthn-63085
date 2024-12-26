# 1
assert 200 > 100
assert [100] * 4 < [100, 100, 100, 10000]
assert sum([1, 3, 5]) == sum([6, 3])
assert max(3, -1, 9) != -1
print("Проверки пройдены")


# 2
def is_person_teenager(age: int) -> bool:
    return 12 <= age <= 17


# 3
from math import factorial
print(factorial(int(input())))


# 4
from typing import List, Literal, TypeAlias, Union
FizzBuzz: TypeAlias = Union[int, Literal["FizzBuzz", "Fizz", "Buzz"]]
def generate_fizz_buzz_list(end: int) -> List[FizzBuzz]:
    result: List[FizzBuzz] = []
    for n in range(1, end + 1):
        if n % 15 == 0:
            result.append("FizzBuzz")
        elif n % 3 == 0:
            result.append("Fizz")
        elif n % 5 == 0:
            result.append("Buzz")
        else:
            result.append(n)
    return result


# 5
def gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return a
end, a = int(input()), int(input())
for _ in range(end - 1):
    b = int(input())
    a = gcd(a, b)
print(a)


# 6
from collections import Counter
def find_duplicate(l: list[int]) -> list[int]:
    counter = Counter(l)
    return list(
        map(
            lambda pair: pair[0],
            filter(lambda pair: pair[1] > 1, counter.most_common()),
        )
    )
assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
assert find_duplicate([1, 2, 3, 4]) == []
assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
print("Все успешно")


# 7
from collections import Counter
def first_unique_char(string: str) -> int:
    counter = Counter(string)
    for index, char in enumerate(string):
        if counter[char] == 1:
            return index
    else:
        return -1
print(first_unique_char(input()))


# 8
from typing import Dict, List, Literal
def format_name_list(names: List[Dict[Literal["name"], str]]) -> str:
    return " и ".join([name["name"] for name in names]).replace(
        " и ", ", ", len(names) - 2
    )
assert (
    format_name_list(
        [
            {"name": "Bart"},
            {"name": "Lisa"},
            {"name": "Maggie"},
            {"name": "Homer"},
            {"name": "Marge"},
        ]
    )
    == "Bart, Lisa, Maggie, Homer и Marge"
)
assert (
    format_name_list(
        [
            {"name": "Bart"},
            {"name": "Lisa"},
            {"name": "Maggie"},
        ]
    )
    == "Bart, Lisa и Maggie"
)
assert (
    format_name_list(
        [
            {"name": "Bart"},
            {"name": "Lisa"},
        ]
    )
    == "Bart и Lisa"
)
assert (
    format_name_list(
        [
            {"name": "Bart"},
        ]
    )
    == "Bart"
)
assert format_name_list([]) == ""
assert (
    format_name_list(
        [
            {"name": "Maggie"},
            {"name": "Lisa"},
            {"name": "Barney"},
            {"name": "Homer"},
            {"name": "Bart"},
            {"name": "Moe"},
        ]
    )
    == "Maggie, Lisa, Barney, Homer, Bart и Moe"
)
assert (
    format_name_list(
        [
            {"name": "Marge"},
            {"name": "Maggie"},
            {"name": "Seymour"},
        ]
    )
    == "Marge, Maggie и Seymour"
)
assert (
    format_name_list(
        [
            {"name": "Maude"},
            {"name": "Bart"},
        ]
    )
    == "Maude и Bart"
)
print("Проверки пройдены")


# 9
from re import fullmatch
def get_domain_name(url: str) -> str:
    match = fullmatch(r"(?:https?:\/\/)?(?:www\.)?([\w-]+)", url)
    if not match:
        raise ValueError()
    return match.group(1)
assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"
assert get_domain_name("http://github.com/carbonfive/raygun") == "github"
assert get_domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert get_domain_name("https://www.siemens.com") == "siemens"
assert get_domain_name("https://www.whatsapp.com") == "whatsapp"
assert get_domain_name("https://www.mywww.com") == "mywww"
print("Проверки пройдены")


# 10
from math import factorial
def trailing_zeros(n: int) -> int:
    counter = 0
    for digit in reversed(str(factorial(n))):
        if digit != "0":
            break
        counter += 1
    return counter
assert trailing_zeros(0) == 0
assert trailing_zeros(6) == 1
assert trailing_zeros(30) == 7
assert trailing_zeros(12) == 2
print("Проверки пройдены")


# 11
from typing import Dict, Tuple
def count_AGTC(sequence: str) -> Tuple[int, int, int, int]:
    counter: Dict[str, int] = {"A": 0, "G": 0, "T": 0, "C": 0}
    for char in sequence:
        counter[char] += 1
    return (counter["A"], counter["G"], counter["T"], counter["C"])
assert count_AGTC("AGGTC") == (1, 2, 1, 1)
assert count_AGTC("AAAATTT") == (4, 0, 3, 0)
assert count_AGTC("AGTTTTT") == (1, 1, 5, 0)
assert count_AGTC("CCT") == (0, 0, 1, 2)
print("Проверки пройдены")
