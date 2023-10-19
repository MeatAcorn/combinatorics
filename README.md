
# Combinatorial Exploration Library

This library is a meticulous exploration of combinatorial concepts through Python code. It encapsulates a myriad of functions to handle permutations and combinations in both ordered and unordered, repeat and no-repeat scenarios.

The history of this started with the question of studying the distribution of combinations in an ordered list of combinations, for instance if you wanted to plot a curve of lottery numbers drawn versus possible to measure is randomness, standard deviation, etc. You could enumerate the whole list and store it in memory, or to a file which could be loaded or iterated, for smaller sets especially. But, we don't do this for natural numbers, if you want to know which number is at position 100 in the natural numbers, than number is '100', the position tells you the symbols and vice versa. Also, larger combinatoric systems are intractable or inefficient due to size, for larger lotteries there are billions of combinations and for anything truly large like genomic sequences in a population, it approaches impossibility. One case in this library, unordered permutations allowing repetitions, is in fact similar to the encoding of normal integers, in that the solution is simply to comvert the position or representation string (depending upon whether you seek the resulting string or position) to base N, where N is the length of the list of elements ('0123456789' in base 10-numbers) and using the members of N as the character set for representing the values, then converting back to decimal (base-10). This is very similar to using hexadecimal numbers, sixteen elements ('0123456789ABCDEF') are the representation character set and the length (16) of the input set are the base, so finding the position of 'FF' results in the integer 256, and finding the value at position 256 (counting from 1, not 0) is 'FF' by simple base conversion. The rest were a bit more complex. 

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
