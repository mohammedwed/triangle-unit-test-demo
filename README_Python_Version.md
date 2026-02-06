# Python Triangle Validator - Unit Testing Assignment

## Overview
This project demonstrates comprehensive unit testing in Python for a triangle validation program. The demo module contains functions to determine if three given sides can form a valid triangle based on the triangle inequality theorem.

## Files Included

### 1. `demo.py`
The main module containing:
- **`is_triangle(a, b, c)`**: Function that validates if three sides form a triangle
- **`main()`**: Interactive command-line interface for user input

### 2. `test_demo.py`
Comprehensive test suite with 24 unit tests using Python's `unittest` framework

## Triangle Inequality Theorem

A valid triangle must satisfy all three conditions:
- a + b > c
- a + c > b
- b + c > a

Where a, b, and c are the lengths of the three sides.

## Test Coverage

### Test Statistics
- **Total Tests**: 24
- **Tests for `is_triangle()`**: 16
- **Tests for `main()`**: 8
- **All tests passing**: ✓

### Test Cases for `is_triangle()` Function

#### Valid Triangles (should return `True`)
1. **Classic right triangle**: `3, 4, 5`
2. **Pythagorean triple**: `5, 12, 13`
3. **Equilateral triangle**: `5, 5, 5`
4. **Isosceles triangle**: `5, 5, 8`
5. **Triangle with floats**: `3.5, 4.5, 5.5`
6. **Large sides**: `100, 150, 200`
7. **Different orderings**: `5, 3, 4` and `4, 5, 3`
8. **Edge case - barely valid**: `2, 3, 4.9`

#### Invalid Triangles (should return `False`)
1. **Degenerate case (sum equals third side)**: `1, 2, 3`
2. **One side too long**: `1, 2, 10`
3. **Extreme disproportion**: `1, 10, 100`
4. **Exact degenerate**: `2, 3, 5`
5. **Floats invalid**: `1.5, 2.5, 10.0`
6. **Different orderings**: `10, 1, 2` and `2, 10, 1`

### Test Cases for `main()` Function

#### Valid Triangle Inputs
- `3, 4, 5` → outputs "This is a triangle."
- `5, 12, 13` → outputs "This is a triangle."
- `7, 7, 7` → outputs "This is a triangle."

#### Invalid Triangle Inputs
- `1, 2, 3` → outputs "This is not a triangle."
- `1, 2, 10` → outputs "This is not a triangle."
- `1, 10, 100` → outputs "This is not a triangle."
- `2, 3, 5` → outputs "This is not a triangle."

#### Input/Output Verification
- Verifies all three prompts appear: "Enter side 1:", "Enter side 2:", "Enter side 3:"

## Testing Approach

### Python unittest Framework
The test suite uses Python's built-in `unittest` framework, which provides:
- Test discovery and organization
- Assertions for validation
- Test fixtures (setUp/tearDown if needed)
- Detailed test reporting

### Test Classes
1. **`TestIsTriangle`**: Contains 16 tests for the `is_triangle()` function
2. **`TestMain`**: Contains 8 tests for the `main()` function

### Mocking and Patching
For testing the `main()` function:
- **`@patch('builtins.input')`**: Simulates user keyboard input
- **`@patch('sys.stdout')`**: Captures console output for verification
- Uses `StringIO` to capture printed output as strings

### Test Organization

Each test method follows Python conventions:
- Named with `test_` prefix
- Descriptive names: `test_<function>_<scenario>_<details>`
- Includes docstrings explaining what is being tested
- Uses descriptive assertion messages

## How to Run the Tests

### Method 1: Using unittest (recommended)
```bash
# Run all tests with verbose output
python3 -m unittest test_demo -v

# Run all tests (simple)
python3 -m unittest test_demo

# Run specific test class
python3 -m unittest test_demo.TestIsTriangle -v

# Run specific test method
python3 -m unittest test_demo.TestIsTriangle.test_is_triangle_valid_triangle_3_4_5 -v
```

### Method 2: Direct execution
```bash
# Run the test file directly
python3 test_demo.py
```

### Method 3: Using pytest (if installed)
```bash
# Install pytest first
pip install pytest

# Run with pytest
pytest test_demo.py -v

# Run with coverage
pytest test_demo.py --cov=demo --cov-report=html
```

## How to Run the Main Program

```bash
python3 demo.py
```

Example interaction:
```
Enter side 1: 
3
Enter side 2: 
4
Enter side 3: 
5
This is a triangle.
```

## Test Output Example

```
test_is_triangle_valid_triangle_3_4_5 ... ok
test_is_triangle_valid_triangle_5_12_13 ... ok
test_is_triangle_valid_equilateral_triangle ... ok
test_is_triangle_valid_isosceles_triangle ... ok
test_is_triangle_invalid_triangle_1_2_3 ... ok
test_is_triangle_invalid_triangle_1_2_10 ... ok
test_is_triangle_invalid_triangle_1_10_100 ... ok
test_is_triangle_edge_case_almost_degenerate ... ok
test_is_triangle_edge_case_degenerate ... ok
test_is_triangle_with_floats_valid_triangle ... ok
test_is_triangle_with_floats_invalid_triangle ... ok
test_is_triangle_large_sides ... ok
test_is_triangle_different_order_valid_1 ... ok
test_is_triangle_different_order_valid_2 ... ok
test_is_triangle_different_order_invalid_1 ... ok
test_is_triangle_different_order_invalid_2 ... ok
test_main_valid_triangle_3_4_5 ... ok
test_main_valid_triangle_5_12_13 ... ok
test_main_valid_equilateral_triangle ... ok
test_main_invalid_triangle_1_2_3 ... ok
test_main_invalid_triangle_1_2_10 ... ok
test_main_invalid_triangle_1_10_100 ... ok
test_main_prompts_for_input ... ok
test_main_edge_case_degenerate_triangle ... ok

----------------------------------------------------------------------
Ran 24 tests in 0.003s

OK
```

## Key Testing Principles Applied

1. **Boundary Testing**: Tests edge cases like degenerate triangles where the sum of two sides equals the third
2. **Equivalence Partitioning**: Tests are grouped into valid and invalid triangle categories
3. **Input Variation**: Tests use integers, floats, small values, and large values
4. **Order Independence**: Verifies that the order of sides doesn't affect the result
5. **Black Box Testing**: Tests focus on inputs and outputs without examining internal implementation
6. **Integration Testing**: The `main()` tests verify the complete user interaction flow
7. **Mocking**: Uses unittest.mock to isolate function behavior and test I/O operations

## Code Quality Features

### demo.py
- Clear function documentation with docstrings
- Type hints in docstrings for clarity
- Simple, readable logic
- Follows PEP 8 style guidelines

### test_demo.py
- Comprehensive test coverage
- Clear test names and documentation
- Proper use of mocking for I/O testing
- Descriptive assertion messages
- Well-organized test classes

## Requirements

- Python 3.6 or higher
- No external dependencies for basic usage
- Optional: pytest for alternative test runner

## Project Structure

```
.
├── demo.py          # Main module with triangle validation logic
├── test_demo.py     # Comprehensive unit test suite
└── README.md        # This file
```

## Extension Ideas

For learning purposes, you could extend this project with:
1. Add error handling for negative or zero side lengths
2. Add tests for invalid input types (strings, None, etc.)
3. Add a function to determine triangle type (equilateral, isosceles, scalene)
4. Add perimeter and area calculations
5. Create a GUI version with corresponding GUI tests
6. Add property-based testing using the `hypothesis` library
7. Add performance tests for large datasets

## Learning Outcomes

This assignment demonstrates:
- Writing testable Python code
- Using Python's unittest framework
- Mocking and patching for I/O testing
- Test organization and naming conventions
- Comprehensive test coverage strategies
- Boundary testing and edge case handling
- Test-driven development principles

## Notes

- All 24 tests pass successfully
- The `is_triangle()` function correctly implements the triangle inequality theorem
- Tests are designed to be comprehensive yet readable
- The test suite properly handles I/O mocking to test console-based programs
- Tests can be run individually or as a complete suite
