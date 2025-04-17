from typing import List, Tuple, Dict

# Variable declarations with type hints
n: int = 5
name: str = "sdfg"

# Function with type hints for parameters and return type
def add(a: int, b: int) -> int:
    return a + b

# List of integers
num_list: List[int] = [1, 2, 3, 4, 5, 6]

# Tuple with a string and an integer
my_tuple: Tuple[str, int] = ("asdfg", 50)

# Dictionary with int keys and string values
my_dict: Dict[int, str] = {
    1: "a",
    2: "b"
}

# Output
print("Sum:", add(3, 3))
print("List:", num_list)
print("Tuple:", my_tuple)
print("Dictionary:", my_dict)
