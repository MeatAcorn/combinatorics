import pytest
from typing import List, Any, Union
from combinations.unordered.with_repeat import combination_at_position_unordered_repeat

# Test data
test_data = [
    (['A', 'B', 'C'], 5, 1, ['A', 'A', 'A', 'A', 'A']),
    (['A', 'B', 'C'], 5, 2, ['A', 'A', 'A', 'A', 'B']),
    (['A', 'B', 'C'], 5, 6, ['A', 'A', 'A', 'B', 'C']),
    (['A', 'B', 'C'], 5, 21, ['A', 'A', 'C', 'A', 'C']),
    (['A', 'B', 'C'], 5, 27, ['A', 'A', 'C', 'C', 'C']),
    (['A', 'B', 'C'], 5, 216, ['C', 'B', 'C', 'C', 'C']),
    (['A', 'B', 'C'], 5, 243, ['C', 'C', 'C', 'C', 'C']),
]

@pytest.mark.parametrize('full_set,choose,position,expected', test_data)
def test_combination_at_position_unordered_repeat(full_set: Any, choose: Any, position: Any, expected: Any):
    result = combination_at_position_unordered_repeat(full_set, position, choose)
    assert result == expected, f'expected {expected}, but got {result}'

