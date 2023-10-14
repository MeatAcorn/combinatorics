import pytest
from permutations.unordered.with_repeat import position_of_permutation_unordered_repeat


@pytest.mark.parametrize("full_set, permutation, expected", [
    (['A', 'B', 'C'], ['A', 'A'], 1),
    (['A', 'B', 'C'], ['A', 'B'], 2),
    (['A', 'B', 'C'], ['A', 'C'], 3),
    (['A', 'B', 'C'], ['B', 'A'], 4),
    (['A', 'B', 'C'], ['B', 'B'], 5),
    (['A', 'B', 'C'], ['B', 'C'], 6),
    (['A', 'B', 'C'], ['C', 'A'], 7),
    (['A', 'B', 'C'], ['C', 'B'], 8),
    (['A', 'B', 'C'], ['C', 'C'], 9)
])
def test_position_of_permutation_unordered_repeat(full_set, permutation, expected):
    result = position_of_permutation_unordered_repeat(full_set, permutation)
    assert result == expected, f"For full_set={full_set}, permutation={permutation}, expected {expected}, got {result}."
