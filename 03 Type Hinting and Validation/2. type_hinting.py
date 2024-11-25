from typing import List, Tuple, Dict, Set, Union, Optional, Any

# type hinting 
# 1. static type hinting <- mypy
# 2. dynamic type hinting or runtime type hinting <- pydantic or python interpreter

def greeting(name: str) -> str:
    return f"Hello, {name}"


print(greeting("John Doe"))

print(greeting(0))

def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))
# print(add(1, '2'))

def average(numbers: List[int]) -> float:
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4, 5]))


# Use Tuple, Dict and set
def get_user() -> Tuple[str, int, str]:
    return ("John Doe", 30, "male")

print(get_user())

def process_user(user: Tuple[str, int, str]) -> None:
    print(f"Name: {user[0]}, Age: {user[1]} Gender: {user[2]}")

process_user(get_user())

def unique_numbers(numbers: List[int]) -> Set[int]:
    return set(numbers)

print(unique_numbers([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))


def get_user_info() -> Dict[str, Union[str, int]]:
    return {"name": "John Doe", "age": 30}

print(get_user_info())


def get_user_info(data: Dict[str, Union[str, int]]) -> None:
    print(f"Name: {data['name']}, Age: {data['age']}")

get_user_info({'name': 'John Doe', 'age': 35})
get_user_info({'name': 'John Doe', 'age': '35'})

def get_user_info(data):
    print(f"Name: {data['name']}, Age: {data['age']}")

get_user_info({'name': 'John Doe', 'age': 35})