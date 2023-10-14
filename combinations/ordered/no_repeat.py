from math import factorial
from typing import Any, List, Union

def position_of_combination_ordered_norepeat(full_set: List[Any], combination: List[Any]) -> Union[int, str]:
    """
    Finds the position of a given k-length combination in the sequence of all possible k-length combinations from the given set.
    The combinations are assumed to be sorted lexicographically and are ordered (i.e., arrangement matters).
    
    Parameters:
    full_set (List[Any]): The list of elements to combine.
    combination (List[Any]): The given combination to find the position of.
    
    Returns:
    Union[int, str]: The position of the given combination in the sequence or an error message if inputs are invalid.
    """
    n = len(full_set)
    k = len(combination)
    # Validation of input
    if k < 1 or n == 0 or k > n:
        return "Invalid inputs."
    # Sort the full set to ensure lexicographic order
    sorted_set = sorted(full_set)
    position = 1  # Initialize position
    for i, elem in enumerate(combination):
        rank = sorted_set.index(elem)  # Rank of the element in the sorted set
        sorted_set = sorted_set[rank+1:]  # Remove used elements from the sorted set
        position += rank * factorial(n - i - 1)  # Update position based on rank and remaining choices  
    return position

def combination_at_position_ordered_norepeat(full_set: List[Any], position: int, k: int) -> Union[List[Any], str]:
    """
    Generates the k-th combination from the given set, assuming the set is ordered and without repetition.
    The combinations are assumed to be sorted lexicographically.
    
    Parameters:
    full_set (List[Any]): The list of elements to combine.
    position (int): The position of the desired combination in the sequence of all possible combinations.
    k (int): The size of each combination.
    
    Returns:
    Union[List[Any], str]: The k-th combination at the given position or an error message if inputs are invalid.
    """
    n = len(full_set)    
    # Validation of input
    if position < 1 or k < 1 or n == 0 or k > n:
        return "Invalid inputs."
    # Sort the full set to ensure lexicographic order
    sorted_set = sorted(full_set)
    # Initialize result list
    result = []
    for i in range(k):
        choices_for_this_position = n - i  # Remaining choices for this position
        combinations_per_choice = factorial(choices_for_this_position - 1) // factorial(choices_for_this_position - k + i)  # Combinations for each choice
        # Determine which element to pick for this position in the combination
        index = (position - 1) // combinations_per_choice
        print('index : {}'.format(index))
        this_choice = sorted_set[index]
        sorted_set = sorted_set[index+1:]  # Remove used elements from the sorted set
        result.append(this_choice)
        # Update the position for the next loop
        position -= index * combinations_per_choice
    return result
