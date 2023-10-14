import pytest
from combinations.ordered.no_repeat import combination_at_position_ordered_norepeat

@pytest.mark.parametrize(
    "full_set, position, k, expected",
    [
        # Add your test cases here.
        # For example:
        (['A', 'B', 'C'], 1, 2, ['A', 'B']),
        (['A', 'B', 'C'], 2, 2, ['A', 'C']),
        (['A', 'B', 'C'], 3, 2, ['B', 'C']),
        # ...
    ],
)
def test_combination_at_position_ordered_norepeat(full_set, position, k, expected):
    assert combination_at_position_ordered_norepeat(full_set, position, k) == expected
