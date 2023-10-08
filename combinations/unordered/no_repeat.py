from typing import Any, List, Union

def combination_at_position_unordered_norepeat(full_set: List[Any], k: int, target_pos: int) -> Union[List[Any], str]:
    """
    Compute the k-combination at a specified position from a given set without repetition.

    Parameters
    ----------
    full_set : List[Any]
        The original set from which combinations are to be generated.
    k : int
        The size of each combination.
    target_pos : int
        The position (1-indexed) of the desired combination.

    Returns
    -------
    Union[List[Any], str]
        The k-combination at the specified position. If the input set is a string, the combination is returned as a string.

    Raises
    ------
    ValueError
        If target_pos is out of bounds.
    """
    def fact(n: int) -> int:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    n = len(full_set)
    out_combination = []
    this_pos = 0
    # Compute comb_subset_lengths once and reuse
    def comb_subset_lengths(n: int, k: int) -> List[int]:
        return [int(fact(n - idx - 1) / (fact(k - 1) * fact(n - idx - k))) for idx in range(n - k + 1)] + [0] * (k - 1)
    # Main loop
    while this_pos < target_pos:
        this_pos += 1
        idx = 0
        full_set_copy = full_set.copy()
        while len(out_combination) < k:
            this_pt = comb_subset_lengths(len(full_set_copy), k - idx)
            pt_sums = [sum(this_pt[:x]) for x in range(1, len(this_pt) + 1)]
            tmp_sum = len([x for x in pt_sums if x <= (target_pos - this_pos)])
            tmp_index = len([x for x in pt_sums if (x + this_pos) <= target_pos])
            if tmp_index:
                out_combination.append(full_set_copy[tmp_index])
                this_pos += sum(this_pt[:tmp_index])
            else:
                out_combination.append(full_set_copy[0])
            full_set_copy = full_set_copy[tmp_index + 1:]
            idx += 1
    # Convert the output to the type of the input iterable
    if isinstance(full_set, str):
        return ''.join(out_combination)
    return out_combination

def position_of_combination_unordered_norepeat(full_set: List[Any], x: List[Any]) -> int:
    """
    Compute the position of a specified k-combination from a given set without repetition.

    Parameters
    ----------
    full_set : List[Any]
        The original set from which combinations are generated.
    x : List[Any]
        The specified k-combination whose position is to be determined.

    Returns
    -------
    int
        The position (1-indexed) of the specified k-combination.

    Raises
    ------
    ValueError
        If the specified combination is not valid or the sets do not align.
    """
    out_pos = 1
    # Factorial function (non-recursive)
    def fact(n: int) -> int:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    n = len(full_set)
    k = len(x)
    # Create a dictionary for quick index look-up
    index_map = {elem: idx for idx, elem in enumerate(full_set)}
    # Compute combSubsetLengths once and reuse
    def comb_subset_lengths(n: int, k: int) -> List[int]:
        return [int(fact(n - idx - 1) / (fact(k - 1) * fact(n - idx - k))) for idx in range(n - k + 1)] + [0] * (k - 1)
    subset_lengths = comb_subset_lengths(n, k)
    # Main loop
    for idx in range(k):
        if x[idx] in index_map:
            elem_idx = index_map[x[idx]]
            # Update out_pos based on the index of x[idx] in fullSet
            if idx < (k - 1):
                out_pos += sum(subset_lengths[:elem_idx])
            else:
                out_pos += elem_idx
            # Remove used elements from full_set and update index_map accordingly
            del index_map[x[idx]]
            full_set = full_set[elem_idx + 1:]
            index_map = {elem: idx for idx, elem in enumerate(full_set)}
            # Update subset_lengths for the reduced fullSet and k
            subset_lengths = comb_subset_lengths(len(full_set), k - idx - 1)
    return out_pos
