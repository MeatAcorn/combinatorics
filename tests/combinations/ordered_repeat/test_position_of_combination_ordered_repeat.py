
from typing import List, Any, Union

# Test cases for the function 'position_of_combination_ordered_repeat'
test_position_of_combination_ordered_repeat = [
    {
        'full_set': ['A', 'B', 'C'],
        'combination': ['A', 'A'],
        'expected': 1
    },
    {
        'full_set': ['A', 'B', 'C'],
        'combination': ['A', 'B'],
        'expected': 2
    },
    {
        'full_set': ['A', 'B', 'C'],
        'combination': ['B', 'A'],
        'expected': 4
    },
    {
        'full_set': ['A', 'B', 'C'],
        'combination': ['C', 'C'],
        'expected': 9
    }
]
