
# Combinatorial Exploration Library

This library is a meticulous exploration of combinatorial concepts through Python code. It encapsulates a myriad of functions to handle permutations and combinations in both ordered and unordered, repeat and no-repeat scenarios.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

Clone this repository to your local machine and navigate to the project directory:

git clone https://github.com/MeatAcorn/combinatorics.git
cd combinatorics


To use the library in your Python projects, simply import the necessary functions:

from combinatorics.permutations.ordered import no_repeat as ordered_permutations_no_repeat
from combinatorics.combinations.unordered import with_repeat as unordered_combinations_with_repeat

## Usage

Each module within this library corresponds to a specific combinatorial operation. Here's a snippet showcasing how to use the library to fetch a specific permutation:

import combinatorics

# Fetch a specific permutation
perm = combinatorics.permutations.ordered.no_repeat.permutation_at_position(['A', 'B', 'C'], 2)
print(perm)  # Output: ['A', 'C']

## Documentation

For a deep dive into the library's capabilities and the mathematical concepts it embodies, refer to the `docs` directory. Additionally, each function is thoroughly documented within the code itself, adhering to PEP 257 guidelines.

## Testing

A comprehensive suite of tests is included to validate the library's functionality. Run the following command from the project root to execute the tests:

python -m unittest discover tests

## Contributing

Although this project primarily serves as a personal exploration, contributions are welcome. Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
