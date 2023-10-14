from math import factorial
from typing import List, Any, Union
from collections import Counter

def position_of_permutation_unordered_repeat(full_set: List[Any], permutation: List[Any]) -> Union[int, str]:
    """
    Finds the position of a given permutation in the sequence of all possible permutations from the given set.
    The permutations are assumed to be sorted lexicographically and are unordered with repetition allowed.
    
    Parameters:
    full_set (List[Any]): The list of elements to permute.
    permutation (List[Any]): The given permutation to find the position of.
    
    Returns:
    Union[int, str]: The position of the given permutation in the sequence or an error message if inputs are invalid.
    """
    n = len(full_set)
    k = len(permutation)
    # Validation of input
    if k < 1 or n == 0:
        return "Invalid inputs."
    # Sort the full set to ensure lexicographic order
    sorted_set = sorted(full_set)
    # Initialize the position counter
    position = 0
    for idx in range(0,k):
        # Compute the number of permutations starting with elements less than elem
        rank = sorted_set.index(permutation[idx])
        # Update the position counter
        position += rank * (n ** (k - idx - 1))
#        position += rank * (1+idx*k)
    return position + 1 # Position in a 1-based index

def permutation_at_position_unordered_repeat(full_set: List[Any], position: int, k: int) -> Union[List[Any], str]:
    """
    Generates the k-th permutation from the given set, assuming the set is unordered and with repetition.
    The permutations are assumed to be sorted lexicographically.
    
    Parameters:
    full_set (List[Any]): The list of elements to permute.
    position (int): The position of the desired permutation in the sequence of all possible permutations.
    k (int): The size of each permutation.
    
    Returns:
    Union[List[Any], str]: The k-th permutation at the given position or an error message if inputs are invalid.
    """
    n = len(full_set)    
    # Validation of input
    if position < 1 or k < 1 or n == 0:
        return "Invalid inputs."
    # Validate if the position is within range
    if position > n ** k:
        return "Position out of range."
    # Sort the full set to ensure lexicographic order
    sorted_set = sorted(full_set)
    # Initialize result list
    result = []
    for i in range(k):
        # Calculate the number of permutations that start with each element
        num_permutations = n ** (k - i - 1)
        # Determine which element to pick for this position in the permutation
        index = (position - 1) // num_permutations
        this_choice = sorted_set[index]
        result.append(this_choice)
        # Update the position for the next loop
        position -= index * num_permutations
    return result
