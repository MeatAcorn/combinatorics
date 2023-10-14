import pytest
from permutations.unordered.no_repeat import permutation_at_position_unordered_norepeat

@pytest.mark.parametrize("test_input, expected", [
    ({"full_set": ['A', 'B', 'C'], "position": 1, "k": 2}, ['A', 'B']),
    ({"full_set": ['A', 'B', 'C'], "position": 2, "k": 2}, ['A', 'C']),
    ({"full_set": ['A', 'B', 'C'], "position": 3, "k": 2}, ['B', 'C']),
    ({"full_set": ['A', 'B', 'C'], "position": 4, "k": 2}, "Position out of range."),
    ({"full_set": [], "position": 1, "k": 2}, "Invalid inputs."),
    ({"full_set": ['A', 'B', 'C'], "position": -1, "k": 2}, "Invalid inputs."),
    ({"full_set": ['A', 'B', 'C'], "position": 1, "k": 0}, "Invalid inputs."),
    ({"full_set": ['A', 'B', 'C'], "position": 1, "k": 4}, "Invalid inputs.")
])

def test_permutation_at_position_unordered_norepeat(test_input, expected):
    result = permutation_at_position_unordered_norepeat(**test_input)
    assert result == expected
