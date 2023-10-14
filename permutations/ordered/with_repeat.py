from typing import List, Any, Union

def permutation_at_position_ordered_repeat(full_set: List[Any], position: int, k: int) -> Union[List[Any], str]:
    """
    Generates the k-length permutation from the given set, considering repetition, based on the specified position.
    The permutations are assumed to be sorted lexicographically.
    
    Parameters:
    full_set (List[Any]): The list of elements to permute.
    position (int): The position of the desired permutation in the sequence of all possible permutations.
    k (int): The size of each permutation.
    
    Returns:
    Union[List[Any], str]: The k-length permutation at the given position or an error message if inputs are invalid.
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
    if position < 1 or k < 1 or n == 0:
        return "Invalid inputs."
    # Initialize result list
    result = base_num(position - 1, n, char_set)
    while len(result) < k:
        result.insert(0, full_set[0])
    return result

def position_of_permutation_ordered_repeat(full_set: List[Any], permutation: List[Any]) -> Union[int, str]:
    """
    Finds the position of a given k-length permutation in the sequence of all possible k-length permutations from the given set.
    The permutations are assumed to be sorted lexicographically.
    
    Parameters:
    full_set (List[Any]): The list of elements to permute.
    permutation (List[Any]): The given permutation to find the position of.
    
    Returns:
    Union[int, str]: The position of the given permutation in the sequence or an error message if inputs are invalid.
    """
    def base_num_to_decimal(digits, b, char_set):
        result = 0
        for digit in digits:
            result = result * b + char_set.index(digit)
        return result
    n = len(full_set)
    k = len(permutation)
    # Sort the full set to ensure lexicographic order
    full_set.sort()
    # Convert to arbitrary base with character set
    char_set = ''.join(full_set)
    # Validation of input
    if k < 1 or n == 0:
        return "Invalid inputs."
    # Convert the permutation to a number in the base 'n'
    position = base_num_to_decimal(permutation, n, char_set) + 1  # Adding 1 as positions are 1-based
    return position
