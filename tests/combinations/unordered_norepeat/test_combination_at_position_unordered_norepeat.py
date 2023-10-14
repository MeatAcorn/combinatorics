import pytest
from combinations.unordered.no_repeat import combination_at_position_unordered_norepeat

@pytest.mark.parametrize(
    "full_set, k, target_pos, expected",
    [
        (['A', 'B', 'C'], 2, 1, ['A', 'B']),
        (['A', 'B', 'C'], 2, 2, ['A', 'C']),
        (['A', 'B', 'C'], 2, 3, ['B', 'C']),
    ]
)
def test_combination_at_position_unordered_norepeat(full_set, k, target_pos, expected):
    assert combination_at_position_unordered_norepeat(full_set, k, target_pos) == expected
