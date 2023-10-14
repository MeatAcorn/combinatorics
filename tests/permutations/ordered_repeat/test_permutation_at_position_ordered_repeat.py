import pytest
from permutations.ordered.with_repeat import permutation_at_position_ordered_repeat


@pytest.mark.parametrize(
    "full_set, position, k, expected",
    [
        # Add your test cases here.
        # For example:
        (['A', 'B', 'C'], 1, 2, ['A', 'A']),
        (['A', 'B', 'C'], 2, 2, ['A', 'B']),
        (['A', 'B', 'C'], 3, 2, ['A', 'C']),
        # ...
    ],
)
def test_permutation_at_position_ordered_repeat(full_set, position, k, expected):
    assert permutation_at_position_ordered_repeat(full_set, position, k) == expected
