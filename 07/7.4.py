# 1
from typing import Final
MIN_DRIVING_AGE: Final = 18
def allowed_driving(name: str, age: int) -> None:
    print(
        f"{name} еще рано садиться за руль"
        if age < MIN_DRIVING_AGE
        else f"{name} может водить"
    )


# 2
from collections import defaultdict
from typing import DefaultDict, Dict, List
def get_word_indices(strings: List[str]) -> Dict[str, List[int]]:
    result: DefaultDict[str, List[int]] = defaultdict(list)
    for index, string in enumerate(strings):
        for word in string.split():
            result[word.lower()].append(index)
    return result
