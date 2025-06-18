# Automated API Testing Script

This script performs automated testing of the Fake Store API endpoint to validate product data and identify defects.

## API Endpoint
- **URL**: https://fakestoreapi.com/products
- **Method**: GET

## Test Objectives

The script validates the following criteria:

1. **HTTP Status Code**: Must be 200 OK
2. **Product Title**: Must be a non-empty string
3. **Product Price**: Must be a non-negative number
4. **Product Rating**: `rating.rate` must be less than or equal to 5

## Setup Instructions

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script**:
   ```bash
   python3 api_test_script.py
   ```

## Expected Output

The script will:
- Display the HTTP status code test result
- Validate each product in the API response
- Print detailed error messages for any products that violate validation rules
- Provide a summary of test results including:
  - Total products tested
  - Number of valid products
  - Number of products with defects
  - Total validation errors found

## Example Output

```
============================================================
AUTOMATED API TESTING SCRIPT
============================================================
Testing endpoint: https://fakestoreapi.com/products

1. Testing HTTP Status Code...
✅ PASSED: HTTP status code is 200 OK

2. Validating Product Data...
Found 20 products to validate

❌ Product 3 has 1 validation error(s):
   - Product 3: Rating exceeds 5 (5.2)

============================================================
TEST SUMMARY
============================================================
Total products tested: 20
Valid products: 19
Products with defects: 1
Total validation errors: 1

DEFECTS FOUND:
------------------------------
• Product 3: Rating exceeds 5 (5.2)
============================================================
```

## Features

- **Comprehensive Validation**: Tests all required fields and data types
- **Detailed Error Reporting**: Clear identification of specific defects
- **Error Handling**: Graceful handling of network errors and malformed responses
- **Type Safety**: Uses type hints for better code maintainability
- **User-Friendly Output**: Clear, formatted output with visual indicators

## Dependencies

- Python 3.6+
- requests library (for HTTP requests) 