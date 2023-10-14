import pytest
from permutations.ordered.no_repeat import position_of_permutation_ordered_norepeat

@pytest.mark.parametrize("test_input, expected", [
    ({'full_set': ['A', 'B', 'C'], 'permutation': ['A', 'B']}, 1),
    ({'full_set': ['A', 'B', 'C'], 'permutation': ['A', 'C']}, 2),
    ({'full_set': ['A', 'B', 'C'], 'permutation': ['B', 'A']}, 3),
    ({'full_set': ['A', 'B', 'C'], 'permutation': ['B', 'C']}, 4),
    ({'full_set': ['A', 'B', 'C'], 'permutation': ['C', 'A']}, 5),
    ({'full_set': ['A', 'B', 'C'], 'permutation': ['C', 'B']}, 6),
    ({'full_set': ['A', 'B', 'C'], 'permutation': ['A', 'B', 'C']}, 1),
    ({'full_set': ['A', 'B', 'C'], 'permutation': ['A', 'C', 'B']}, 2),
    ({'full_set': ['A', 'B', 'C'], 'permutation': ['B', 'A', 'C']}, 3),
    ({'full_set': ['A', 'B', 'C'], 'permutation': ['B', 'C', 'A']}, 4),
    ({'full_set': ['A', 'B', 'C'], 'permutation': ['C', 'A', 'B']}, 5),
    ({'full_set': ['A', 'B', 'C'], 'permutation': ['C', 'B', 'A']}, 6),
])
def test_position_of_permutation_ordered_norepeat(test_input, expected):
    result = position_of_permutation_ordered_norepeat(**test_input)
    assert result == expected
