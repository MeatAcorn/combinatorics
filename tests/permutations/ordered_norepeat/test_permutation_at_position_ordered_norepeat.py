import pytest
from permutations.ordered.no_repeat import permutation_at_position_ordered_norepeat

@pytest.mark.parametrize("test_input, expected", [
    ({"full_set": [], "position": 1, "k": 2}, "Invalid inputs."),
    ({"full_set": ['A', 'B', 'C'], "position": -1, "k": 2}, "Invalid inputs."),
    ({"full_set": ['A', 'B', 'C'], "position": 1, "k": 0}, "Invalid inputs."),
    ({"full_set": ['A', 'B', 'C'], "position": 1, "k": 4}, "Invalid inputs."),
    ({"full_set": ['A', 'B', 'C'], "position": 1, "k": 2}, ['A', 'B']),
    ({"full_set": ['A', 'B', 'C'], "position": 2, "k": 2}, ['A', 'C']),
    ({"full_set": ['A', 'B', 'C'], "position": 3, "k": 2}, ['B', 'A']),
    ({"full_set": ['A', 'B', 'C'], "position": 4, "k": 2}, ['B', 'C']),
    ({"full_set": ['A', 'B', 'C'], "position": 5, "k": 2}, ['C', 'A']),
    ({"full_set": ['A', 'B', 'C'], "position": 6, "k": 2}, ['C', 'B']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 1, "k": 3}, ['A', 'B', 'C']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 2, "k": 3}, ['A', 'B', 'D']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 3, "k": 3}, ['A', 'C', 'B']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 4, "k": 3}, ['A', 'C', 'D']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 5, "k": 3}, ['A', 'D', 'B']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 6, "k": 3}, ['A', 'D', 'C']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 7, "k": 3}, ['B', 'A', 'C']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 8, "k": 3}, ['B', 'A', 'D']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 9, "k": 3}, ['B', 'C', 'A']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 10, "k": 3}, ['B', 'C', 'D']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 11, "k": 3}, ['B', 'D', 'A']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 12, "k": 3}, ['B', 'D', 'C']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 13, "k": 3}, ['C', 'A', 'B']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 14, "k": 3}, ['C', 'A', 'D']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 15, "k": 3}, ['C', 'B', 'A']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 16, "k": 3}, ['C', 'B', 'D']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 17, "k": 3}, ['C', 'D', 'A']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 18, "k": 3}, ['C', 'D', 'B']), 
    ({"full_set": ['A', 'B', 'C','D'], "position": 19, "k": 3}, ['D', 'A', 'B']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 20, "k": 3}, ['D', 'A', 'C']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 21, "k": 3}, ['D', 'B', 'A']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 22, "k": 3}, ['D', 'B', 'C']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 23, "k": 3}, ['D', 'C', 'A']),
    ({"full_set": ['A', 'B', 'C','D'], "position": 24, "k": 3}, ['D', 'C', 'B']),
])

def test_permutation_at_position_ordered_norepeat(test_input, expected):
    result = permutation_at_position_ordered_norepeat(**test_input)
    assert result == expected

