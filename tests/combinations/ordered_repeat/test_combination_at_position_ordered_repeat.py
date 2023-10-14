import pytest
from typing import List, Any
from combinations.ordered.with_repeat import combination_at_position_ordered_repeat

test_data = [{'full_set': ['A', 'B', 'C'], 'position': 1, 'k': 2, 'expected': ['A', 'A']}, {'full_set': ['A', 'B', 'C'], 'position': 4, 'k': 2, 'expected': ['B', 'A']}, {'full_set': ['A', 'B', 'C'], 'position': 9, 'k': 2, 'expected': ['C', 'C']}, {'full_set': ['A', 'B', 'C'], 'position': 27, 'k': 3, 'expected': ['C', 'C', 'C']}]

@pytest.mark.parametrize("full_set, position, k, expected", [(x['full_set'], x['position'], x['k'], x['expected']) for x in test_data])
def test_combination_at_position_ordered_repeat(full_set: Any, position: Any, k: Any, expected: Any):
    assert combination_at_position_ordered_repeat(full_set, position, k) == expected
