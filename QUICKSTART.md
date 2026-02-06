# Quick Start Guide - Python Triangle Validator

## Setup (No installation needed!)

This project uses only Python's standard library, so no additional packages are required.

### Prerequisites
- Python 3.6 or higher

### Verify Python Installation
```bash
python3 --version
```

## Running the Program

### Interactive Mode
```bash
python3 demo.py
```

Then enter three numbers when prompted:
```
Enter side 1: 
3
Enter side 2: 
4
Enter side 3: 
5
This is a triangle.
```

### Using the Function Directly
```python
from demo import is_triangle

# Check if sides form a triangle
result = is_triangle(3, 4, 5)
print(result)  # True

result = is_triangle(1, 2, 10)
print(result)  # False
```

## Running the Tests

### Basic Test Run
```bash
python3 -m unittest test_demo
```

### Verbose Output (Recommended)
```bash
python3 -m unittest test_demo -v
```

### Run Specific Test Class
```bash
# Test only is_triangle function
python3 -m unittest test_demo.TestIsTriangle -v

# Test only main function
python3 -m unittest test_demo.TestMain -v
```

### Run Single Test
```bash
python3 -m unittest test_demo.TestIsTriangle.test_is_triangle_valid_triangle_3_4_5
```

## Optional: Enhanced Testing with pytest

If you want better test output and coverage reports:

### 1. Install pytest (optional)
```bash
pip install pytest pytest-cov
```

### 2. Run tests with pytest
```bash
# Simple run
pytest test_demo.py

# Verbose with details
pytest test_demo.py -v

# With coverage report
pytest test_demo.py --cov=demo

# Generate HTML coverage report
pytest test_demo.py --cov=demo --cov-report=html
```

### 3. View coverage report
After generating HTML report:
```bash
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

## Expected Output

### Successful Test Run
```
test_is_triangle_different_order_invalid_1 ... ok
test_is_triangle_different_order_invalid_2 ... ok
test_is_triangle_different_order_valid_1 ... ok
test_is_triangle_different_order_valid_2 ... ok
test_is_triangle_edge_case_almost_degenerate ... ok
test_is_triangle_edge_case_degenerate ... ok
test_is_triangle_invalid_triangle_1_10_100 ... ok
test_is_triangle_invalid_triangle_1_2_10 ... ok
test_is_triangle_invalid_triangle_1_2_3 ... ok
test_is_triangle_large_sides ... ok
test_is_triangle_valid_equilateral_triangle ... ok
test_is_triangle_valid_isosceles_triangle ... ok
test_is_triangle_valid_triangle_3_4_5 ... ok
test_is_triangle_valid_triangle_5_12_13 ... ok
test_is_triangle_with_floats_invalid_triangle ... ok
test_is_triangle_with_floats_valid_triangle ... ok
test_main_edge_case_degenerate_triangle ... ok
test_main_invalid_triangle_1_10_100 ... ok
test_main_invalid_triangle_1_2_10 ... ok
test_main_invalid_triangle_1_2_3 ... ok
test_main_prompts_for_input ... ok
test_main_valid_equilateral_triangle ... ok
test_main_valid_triangle_3_4_5 ... ok
test_main_valid_triangle_5_12_13 ... ok

----------------------------------------------------------------------
Ran 24 tests in 0.003s

OK
```

## Troubleshooting

### Issue: "No module named 'demo'"
**Solution**: Make sure you're running the tests from the same directory as demo.py and test_demo.py

### Issue: "ModuleNotFoundError: No module named 'pytest'"
**Solution**: Either install pytest (`pip install pytest`) or use unittest instead:
```bash
python3 -m unittest test_demo -v
```

### Issue: Tests fail with import errors
**Solution**: Ensure Python 3.6+ is being used:
```bash
python3 --version
```

## File Structure
```
your-project-folder/
├── demo.py              # Main program
├── test_demo.py         # Test suite
├── README.md            # Full documentation
├── QUICKSTART.md        # This file
└── requirements.txt     # Optional dependencies
```

## Next Steps

1. ✅ Run the program: `python3 demo.py`
2. ✅ Run the tests: `python3 -m unittest test_demo -v`
3. ✅ Verify all 24 tests pass
4. 📚 Read the full README.md for detailed documentation
5. 🔧 Try modifying the code and tests to learn more

## Common Test Commands Cheat Sheet

```bash
# Run all tests (simple)
python3 -m unittest test_demo

# Run all tests (verbose)
python3 -m unittest test_demo -v

# Run only is_triangle tests
python3 -m unittest test_demo.TestIsTriangle -v

# Run only main function tests
python3 -m unittest test_demo.TestMain -v

# Run the actual program
python3 demo.py

# With pytest (if installed)
pytest test_demo.py -v
pytest test_demo.py --cov=demo
```

## Understanding Test Results

- **ok**: Test passed ✓
- **FAIL**: Test failed - assertion was false
- **ERROR**: Test had an exception/error
- **Ran X tests**: Total number of tests executed
- **OK**: All tests passed!

## Tips for Learning

1. Try breaking the code intentionally to see tests fail
2. Add your own test cases
3. Modify the is_triangle function and watch tests fail/pass
4. Read the test code to understand how mocking works
5. Experiment with different input values

Happy testing! 🎉
