from typing import List, Any, Union, Optional
from math import comb
from collections import Counter

def combination_at_position_unordered_repeat(full_set: List[Any], position: int, k: Optional[int] = None) -> Union[List[Any], str]:
    """
    Generates the k-th combination from the given set, considering repetition, based on the specified position.
    The combinations are assumed to be sorted lexicographically.
    
    Parameters:
    full_set (List[Any]): The list of elements to combine.
    position (int): The position of the desired combination in the sequence of all possible combinations.
    k (Optional[int]): The size of each combination. If not specified, the function won't pad the output.
    
    Returns:
    Union[List[Any], str]: The k-th combination at the given position or an error message if inputs are invalid.
    """
    def base_num(n, b, char_set):
        if n == 0:
            return [char_set[0]]
        digits = []
        while n:
            digits.append(char_set[n % b])
            n //= b
        return digits[::-1]
    n = len(full_set)
    # Sort the full set to ensure lexicographic order
    full_set.sort()
    # Convert to arbitrary base with character set
    char_set = ''.join(full_set)
    # Validation of input
    if position < 1 or (k is not None and k < 1) or n == 0:
        return "Invalid inputs."
    # Initialize result list
    result = base_num(position - 1, n, char_set)
    if k is not None:
        while len(result) < k:
            result.insert(0, full_set[0])
    return result

def position_of_combination_unordered_repeat(full_set: List[Any], combination: List[Any]) -> Union[int, str]:
    """
    Finds the position of a given k-th combination in the sequence of all possible k-th combinations from the given set.
    The combinations are assumed to be sorted lexicographically.
    
    Parameters:
    full_set (List[Any]): The list of elements to combine.
    combination (List[Any]): The given combination to find the position of.
    
    Returns:
    Union[int, str]: The position of the given combination in the sequence or an error message if inputs are invalid.
    """
    def base_num_to_decimal(digits, b, char_set):
        result = 0
        for digit in digits:
            result = result * b + char_set.index(digit)
        return result
    n = len(full_set)
    k = len(combination)
    # Sort the full set to ensure lexicographic order
    full_set.sort()
    # Convert to arbitrary base with character set
    char_set = ''.join(full_set)
    # Validation of input
    if k < 1 or n == 0:
        return "Invalid inputs."
    # Convert the combination to a number in the base 'n'
    position = base_num_to_decimal(combination, n, char_set) + 1  # Adding 1 as positions are 1-based
    return position
