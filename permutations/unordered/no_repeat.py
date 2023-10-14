from typing import List, Any, Union
from math import factorial

def permutation_at_position_unordered_norepeat(full_set: List[Any], position: int, k: int) -> Union[List[Any], str]:
    """
    Generates the k-length permutation at the given position from the full_set, assuming the permutations are unordered and without repetition.
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
        permutations_per_choice = factorial(n - i - 1) // factorial(n - k + i)
        if permutations_per_choice == 0:
            permutations_per_choice = 1
        # Determine which element to pick for this position in the permutation
        index = (position - 1) // permutations_per_choice
        # Check if index is within the length of sorted_set
        if index >= len(sorted_set):
            return "Position out of range."
        this_choice = sorted_set[index]
        # Remove all elements <= this_choice from the sorted set
        sorted_set = [x for x in sorted_set if x > this_choice]
        # Append the chosen element to the result
        result.append(this_choice)
        # Update the position for the next loop
        position -= index * permutations_per_choice
    return result

def position_of_permutation_unordered_norepeat(full_set: List[Any], permutation: List[Any]) -> Union[int, str]:
    """
    Finds the position of a given k-length permutation in the sequence of all k-length permutations
    formed from the full_set, assuming the permutations are unordered and without repetition.
    The permutations are assumed to be sorted lexicographically.

    Parameters:
    full_set (List[Any]): The list of elements to permute.
    permutation (List[Any]): The k-length permutation whose position is to be found.

    Returns:
    Union[int, str]: The position of the permutation in the sequence or an error message if inputs are invalid.
    """
    # Validate the inputs
    n = len(full_set)
    k = len(permutation)
    if k < 1 or k > n or n == 0:
        return "Invalid inputs."
    # Check if the permutation is valid
    sorted_set = sorted(full_set)
    if [_ for _ in permutation if _ not in full_set]:
        return "Invalid permutation."
    # Initialize the position counter and make a copy of the sorted full set
    position = 1  # Starting from 1 as per the 1-based indexing in the problem statement
    sorted_set = sorted(full_set)
    for element in permutation:
        # Find the index of the current element in the sorted set
        index = sorted_set.index(element)
        # Calculate the number of permutations starting with each remaining element
        permutations_per_choice = factorial(n - 1) // factorial(n - k)
        # Add the number of permutations skipped due to the current element
        position += index * permutations_per_choice
        # Remove the element from the sorted set
        sorted_set.remove(element)
        # Update n and k for the next loop
        n -= 1
        k -= 1
    return position
