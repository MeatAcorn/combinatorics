import pytest
from permutations.ordered.with_repeat import position_of_permutation_ordered_repeat


@pytest.mark.parametrize(
    "full_set, permutation, expected",
    [
        # Add your test cases here.
        # For example:
        (['A', 'B', 'C'], ['A', 'A'], 1),
        (['A', 'B', 'C'], ['A', 'B'], 2),
        (['A', 'B', 'C'], ['A', 'C'], 3),
        # ...
    ],
)
def test_position_of_permutation_ordered_repeat(full_set, permutation, expected):
    assert position_of_permutation_ordered_repeat(full_set, permutation) == expected
