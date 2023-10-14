import pytest
from combinations.unordered.with_repeat import position_of_combination_unordered_repeat

# Test data
test_data = [
    (['A', 'B', 'C'], ['A', 'A', 'A', 'A', 'A'], 1),
    (['A', 'B', 'C'], ['A', 'A', 'A', 'A', 'B'], 2),
    (['A', 'B', 'C'], ['A', 'A', 'A', 'B', 'C'], 6),
    (['A', 'B', 'C'], ['A', 'A', 'C', 'A', 'C'], 21),
    (['A', 'B', 'C'], ['C', 'C', 'C', 'C', 'C'], 243),
]

@pytest.mark.parametrize('full_set,combination,expected', test_data)
def test_position_of_combination_unordered_repeat(full_set, combination, expected):
    result = position_of_combination_unordered_repeat(full_set, combination)
    assert result == expected, f'expected {expected}, but got {result}'

