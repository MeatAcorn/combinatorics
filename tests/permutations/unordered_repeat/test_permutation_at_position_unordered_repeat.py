import pytest
from permutations.unordered.with_repeat import permutation_at_position_unordered_repeat

# Test cases for the permutation_at_position_unordered_repeat function
@pytest.mark.parametrize("test_input, expected", [
    ({"full_set": ['A', 'B', 'C'], "position": 1, "k": 2}, ['A', 'A']),
    ({"full_set": ['A', 'B', 'C'], "position": 2, "k": 2}, ['A', 'B']),
    ({"full_set": ['A', 'B', 'C'], "position": 3, "k": 2}, ['A', 'C']),
    ({"full_set": ['A', 'B', 'C'], "position": 4, "k": 2}, ['B', 'A']),
    ({"full_set": ['A', 'B', 'C'], "position": 5, "k": 2}, ['B', 'B']),
    ({"full_set": ['A', 'B', 'C'], "position": 6, "k": 2}, ['B', 'C']),
    ({"full_set": ['A', 'B', 'C'], "position": 7, "k": 2}, ['C', 'A']),
    ({"full_set": ['A', 'B', 'C'], "position": 8, "k": 2}, ['C', 'B']),
    ({"full_set": ['A', 'B', 'C'], "position": 9, "k": 2}, ['C', 'C']),
    ({"full_set": ['A', 'B', 'C'], "position": 10, "k": 2}, "Position out of range."),
    ({"full_set": [], "position": 1, "k": 2}, "Invalid inputs."),
    ({"full_set": ['A', 'B', 'C'], "position": -1, "k": 2}, "Invalid inputs."),
    ({"full_set": ['A', 'B', 'C'], "position": 1, "k": 0}, "Invalid inputs.")
])
def test_permutation_at_position_unordered_repeat(test_input, expected):
    result = permutation_at_position_unordered_repeat(**test_input)
    assert result == expected
