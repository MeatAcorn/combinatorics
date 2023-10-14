import pytest
from combinations.unordered.no_repeat import position_of_combination_unordered_norepeat

@pytest.mark.parametrize(
    "full_set, combination, expected",
    [
        (['A', 'B', 'C'], ['A', 'B'], 1),
        (['A', 'B', 'C'], ['A', 'C'], 2),
        (['A', 'B', 'C'], ['B', 'C'], 3),
    ]
)
def test_position_of_combination_unordered_norepeat(full_set, combination, expected):
    assert position_of_combination_unordered_norepeat(full_set, combination) == expected
