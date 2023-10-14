import pytest
from permutations.unordered.no_repeat import position_of_permutation_unordered_norepeat

@pytest.mark.parametrize("test_input, expected", [
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['A','B','C']}, 1),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['A','B','D']}, 2),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['A','C','B']}, 3),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['A','C','D']}, 4),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['A','D','B']}, 5),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['A','D','C']}, 6),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['B','A','C']}, 7),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['B','A','D']}, 8),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['B','C','A']}, 9),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['B','C','D']}, 10),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['B','D','A']}, 11),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['B','D','C']}, 12),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['C','A','B']}, 13),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['C','A','D']}, 14),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['C','B','A']}, 15),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['C','B','D']}, 16),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['C','D','A']}, 17),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['C','D','B']}, 18),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['D','A','B']}, 19),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['D','A','C']}, 20),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['D','B','A']}, 21),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['D','B','C']}, 22),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['D','C','A']}, 23),
    ({"full_set": ['A', 'B', 'C','D'], "permutation": ['D','C','B']}, 24),    
    ({"full_set": [], "permutation": ['A', 'B']}, "Invalid inputs."),
    ({"full_set": ['A', 'B', 'C'], "permutation": []}, "Invalid inputs."),
    ({"full_set": ['A', 'B', 'C'], "permutation": ['A', 'B', 'D']}, "Invalid permutation.")
])
def test_position_of_permutation_unordered_norepeat(test_input, expected):
    result = position_of_permutation_unordered_norepeat(**test_input)
    assert result == expected


