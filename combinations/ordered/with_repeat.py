from typing import List, Any, Union

def combination_at_position_ordered_repeat(full_set: List[Any], position: int, k: int) -> Union[List[Any], str]:
    """
    Generates the k-th combination from the given set, assuming the set is ordered and allows repetition.
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
    if position < 1 or k < 1 or n == 0:
        return "Invalid inputs."
    # Sort the full set to ensure lexicographic order
    sorted_set = sorted(full_set)
    # Initialize result list
    result = []
    for i in range(k):
        combinations_per_choice = n ** (k - i - 1)  # Combinations for each choice
        # Determine which element to pick for this position in the combination
        index = (position - 1) // combinations_per_choice
        result.append(sorted_set[index])
        # Update the position for the next loop
        position -= index * combinations_per_choice
    return result

def position_of_combination_ordered_repeat(full_set: List[Any], combination: List[Any]) -> Union[int, str]:
    """
    Finds the position of a given k-length combination in the sequence of all possible k-length combinations from the given set.
    The combinations are assumed to be sorted lexicographically and are ordered (i.e., arrangement matters) and allows repetition.
    
    Parameters:
    full_set (List[Any]): The list of elements to combine.
    combination (List[Any]): The given combination to find the position of.
    
    Returns:
    Union[int, str]: The position of the given combination in the sequence or an error message if inputs are invalid.
    """
    n = len(full_set)
    k = len(combination)    
    # Validation of input
    if k < 1 or n == 0:
        return "Invalid inputs."
    # Sort the full set to ensure lexicographic order
    sorted_set = sorted(full_set)
    # Initialize position
    position = 0
    # Iterate over the combination to find the position
    for i, elem in enumerate(combination):
        index = sorted_set.index(elem)  # Get the index of the element in the sorted set
        position += index * (n ** (k - i - 1))  # Update the position based on this index and the remaining choices
    # Convert the position to 1-based index
    position += 1
    return position
