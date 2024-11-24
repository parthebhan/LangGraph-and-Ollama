from typing import List, Tuple, Dict, Set, Union, Optional, Any

# Simple type hinting
def greet(name: str) -> str:
    return f"Hello, {name}!"
print(greet("Alice"))


def add(a: int, b: int) -> int:
    return a + b
print(add(3, 5))


def average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)
print(average([1.0, 2.0, 3.0]))

# Using Tuple, Dict, and Set
def process_data(data: Tuple[int, str, float]) -> Dict[str, Any]:
    return {
        "id": data[0],
        "name": data[1],
        "value": data[2]
    }
print(process_data((1, "example", 3.14)))

def unique_items(items: List[int]) -> Set[int]:
    return set(items)
print(unique_items([1, 2, 2, 3, 4, 4]))

# Using Union and Optional
def get_value(data: Dict[str, Union[int, str]], key: str) -> Optional[Union[int, str]]:
    return data.get(key)
print(get_value({"key1": 42, "key2": "value"}, "key1"))
