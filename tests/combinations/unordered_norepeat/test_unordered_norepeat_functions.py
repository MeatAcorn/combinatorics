import pytest
from combinations.unordered.no_repeat import combination_at_position_unordered_norepeat,position_of_combination_unordered_norepeat

def binomial(n: int, k: int) -> int:
    result = 1
    for i in range(1, k + 1):
        result *= (n - i + 1)
        result //= i
    return result

def test_functions():
    full_set = ['A', 'B', 'C']
    k = 2

    for pos in range(1, binomial(len(full_set), k) + 1):
        # Generate combination
        comb = combination_at_position_unordered_norepeat(full_set, k, pos)
        # Find position
        result_pos = position_of_combination_unordered_norepeat(full_set, comb)
        # Check consistency
        assert result_pos == pos, f"Mismatch at position {pos}: expected {pos} but got {result_pos}"

    # You can add more tests and edge cases as needed
