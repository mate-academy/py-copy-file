from typing import List, Optional

def my_function(param: int) -> str:
    return str(param)

def add_numbers(a: int, b: int) -> int:
    return a + b

def get_user_data(user_id: int) -> Optional[dict]:
    if user_id == 1:
        return {"id": 1, "name": "Alice"}
    return None

def process_data(data: List[int]) -> List[int]:
    return [x * 2 for x in data]
