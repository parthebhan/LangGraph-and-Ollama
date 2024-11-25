from typing import Annotated, get_type_hints, get_origin, get_args

def sqaure(x: Annotated[int, (0, 100)]) -> int:
    """
    Multiplies the input by 2 after validating that it falls within the specified range.

    Args:
        x (Annotated[int, (0, 100)]): The input value to sqaure, constrained to 0 <= x <= 100.

    Returns:
        int: The sqaure value if validation succeeds.

    Raises:
        ValueError: If the input does not fall within the specified range.
    """

    type_hints = get_type_hints(sqaure, include_extras=True) 
    hint = type_hints['x']

    if get_origin(hint) is Annotated:
        hint_type, *hint_args = get_args(hint)
        low, high = hint_args[0]
        if not (low <= x <= high):
            raise ValueError(f"Input value must be between {low} and {high}")
        
    return x * x

print(sqaure(-10))


