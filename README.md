# Binary Calculator

A simple binary calculator that performs operations on binary numbers. This calculator supports addition, subtraction, multiplication, and division and includes proper error handling and formatting. 

## Features

- **Binary Operations:** Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Custom Conversions:** Implements custom logic for converting binary to decimal and decimal to binary.  
- **Error Handling:**
  - Returns `"Error"` for invalid binary inputs (characters other than `0` and `1`).
  - Returns `"NaN"` when a division by zero is attempted.
  - Returns `"Overflow"` for operations that result in negative numbers or numbers that exceed 8 bits.
- **Output:** All outputs are 8-bit binary numbers, padded with leading zeros.

## Requirements

The binary calculator function must be implemented as a function named `binary_calculator()` with three parameters:
- `bin1` - A string representing the first binary number (must be composed only of `0` and `1`).
- `bin2` - A string representing the second binary number (must be composed only of `0` and `1`).
- `operator` - A string containing one of the following arithmetic operators: `'+'`, `'-'`, `'*'`, or `'/'`.

> Note: Do not use Python's built-in `bin()`, implement your own conversion logic.

## Implementation Details

- **Binary-to-Decimal Conversion:** Convert the binary input strings to a decimal number.
- **Decimal-to-Binary Conversion:** Convert the resulting decimal number back to an 8-bit binary string.
- **Rounding:** When needed, rounding down to the nearest whole number (floor division) is applied.
- **Edge Cases:** Make sure to handle cases such as:
  - Binary input strings containing invalid characters.
  - Division by zero.
  - Operations resulting in numbers that are negative or exceed the range of 8 bits.

## Example Usage

```python
result = binary_calculator("00000101", "00000011", "+")
print(result)  # Output should be "00001000"
```

## How to Run

1. Ensure that Python is installed on your system.
2. Place the `binary_calculator()` function in your project file.
3. Run the script in a terminal or within an IDE (e.g., Visual Studio Code).
4. Use the provided test cases or create your own to validate functionality.