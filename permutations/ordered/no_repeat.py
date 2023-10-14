from math import factorial, perm
from typing import List, Union, Any

def permutation_at_position_ordered_norepeat(full_set: List[Any], position: int, k: int) -> Union[List[Any], str]:
    """
    Generates the k-length permutation at the given position from the full_set, assuming the permutations are ordered and without repetition.
    The permutations are assumed to be sorted lexicographically.

    Parameters:
    full_set (List[Any]): The list of elements to permute.
    position (int): The position of the desired permutation in the sequence of all possible permutations.
    k (int): The size of each permutation.

    Returns:
    Union[List[Any], str]: The k-length permutation at the given position or an error message if inputs are invalid.
    """
    # Validate the inputs
    n = len(full_set)
    if position < 1 or k < 1 or k > n or n == 0:
        return "Invalid inputs."
    # Calculate the total number of permutations
    total_permutations = factorial(n) // factorial(n - k)
    if position > total_permutations:
        return "Position out of range."
    # Initialize the result list and the sorted set of available elements
    result = []
    sorted_set = sorted(full_set)
    for i in range(k):
        # Compute the number of permutations starting with each remaining element
        permutations_per_choice = factorial(n - i - 1) // factorial(n - k)
        # Determine which element to pick for this position in the permutation
        index, position = divmod(position - 1, permutations_per_choice)
        # Append the selected element to the result and remove it from the sorted set
        result.append(sorted_set.pop(index))
        # Update the position for the next loop
        position += 1
    return result

def position_of_permutation_ordered_norepeat(full_set: List[Any], permutation: List[Any]) -> Union[int, str]:
    """
    Finds the position of a given k-length permutation in the sequence of all k-length permutations generated from the full_set.
    The permutations are assumed to be ordered and without repetition, sorted lexicographically.

    Parameters:
    full_set (List[Any]): The list of elements to permute.
    permutation (List[Any]): The target permutation.

    Returns:
    Union[int, str]: The position of the permutation in the sequence or an error message if inputs are invalid.
    """
    # Validate the inputs
    n = len(full_set)
    k = len(permutation)
    if k < 1 or k > n or n == 0:
        return "Invalid inputs."        
    if [_ for _ in permutation if _ not in full_set]:
        return "Invalid permutation."
    # Initialize the position counter and sort the full set
    position = 1
    sorted_set = sorted(full_set)
    for i in range(k):
        # Compute the number of permutations starting with each remaining element
        permutations_per_choice = factorial(n - i - 1) // factorial(n - k + i)
        # Find the index of the i-th element of the permutation in the sorted set
        index = sorted_set.index(permutation[i])
        # Update the position counter
        if not permutations_per_choice:
            position += index
        else:
            position += index * permutations_per_choice
        # Remove the selected element from the sorted set
        sorted_set.pop(index)
    return position
