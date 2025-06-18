#!/usr/bin/env python3
"""
Automated API Testing Script for Fake Store API
Tests the endpoint: https://fakestoreapi.com/products

This script validates:
1. HTTP status code (must be 200 OK)
2. Product title must be a non-empty string
3. Product price must be a non-negative number
4. Product rating.rate must be less than or equal to 5
"""

import requests
import json
from typing import List, Dict, Any


def test_api_endpoint(url: str) -> Dict[str, Any]:
    """
    Test the API endpoint and return the response data.
    
    Args:
        url (str): The API endpoint URL
        
    Returns:
        Dict containing response status, data, and any errors
    """
    try:
        response = requests.get(url, timeout=10)
        return {
            'status_code': response.status_code,
            'data': response.json() if response.status_code == 200 else None,
            'error': None
        }
    except requests.exceptions.RequestException as e:
        return {
            'status_code': None,
            'data': None,
            'error': f"Request failed: {str(e)}"
        }
    except json.JSONDecodeError as e:
        return {
            'status_code': response.status_code,
            'data': None,
            'error': f"JSON decode error: {str(e)}"
        }


def validate_product(product: Dict[str, Any], product_id: int) -> List[str]:
    """
    Validate a single product object against the defined rules.
    
    Args:
        product (Dict): Product object to validate
        product_id (int): Product ID for reference
        
    Returns:
        List of validation errors found
    """
    errors = []
    
    # Validate title (must be a non-empty string)
    if 'title' not in product:
        errors.append(f"Product {product_id}: Missing title field")
    elif not isinstance(product['title'], str):
        errors.append(f"Product {product_id}: Title is not a string (type: {type(product['title']).__name__})")
    elif not product['title'].strip():
        errors.append(f"Product {product_id}: Empty title")
    
    # Validate price (must be a non-negative number)
    if 'price' not in product:
        errors.append(f"Product {product_id}: Missing price field")
    elif not isinstance(product['price'], (int, float)):
        errors.append(f"Product {product_id}: Price is not a number (type: {type(product['price']).__name__})")
    elif product['price'] < 0:
        errors.append(f"Product {product_id}: Negative price ({product['price']})")
    
    # Validate rating.rate (must be less than or equal to 5)
    if 'rating' not in product:
        errors.append(f"Product {product_id}: Missing rating field")
    elif not isinstance(product['rating'], dict):
        errors.append(f"Product {product_id}: Rating is not an object (type: {type(product['rating']).__name__})")
    elif 'rate' not in product['rating']:
        errors.append(f"Product {product_id}: Missing rating.rate field")
    elif not isinstance(product['rating']['rate'], (int, float)):
        errors.append(f"Product {product_id}: Rating.rate is not a number (type: {type(product['rating']['rate']).__name__})")
    elif product['rating']['rate'] > 5:
        errors.append(f"Product {product_id}: Rating exceeds 5 ({product['rating']['rate']})")
    
    return errors


def run_api_tests() -> None:
    """
    Main function to run all API tests and display results.
    """
    api_url = "https://fakestoreapi.com/products"
    
    print("=" * 60)
    print("AUTOMATED API TESTING SCRIPT")
    print("=" * 60)
    print(f"Testing endpoint: {api_url}")
    print()
    
    # Test 1: Verify HTTP status code
    print("1. Testing HTTP Status Code...")
    response_data = test_api_endpoint(api_url)
    
    if response_data['error']:
        print(f"❌ ERROR: {response_data['error']}")
        return
    
    if response_data['status_code'] != 200:
        print(f"❌ FAILED: Expected status code 200, got {response_data['status_code']}")
        return
    else:
        print(f"✅ PASSED: HTTP status code is {response_data['status_code']} OK")
    
    print()
    
    # Test 2: Validate product data
    print("2. Validating Product Data...")
    products = response_data['data']
    
    if not isinstance(products, list):
        print(f"❌ ERROR: Expected list of products, got {type(products).__name__}")
        return
    
    print(f"Found {len(products)} products to validate")
    print()
    
    all_errors = []
    valid_products = 0
    
    for i, product in enumerate(products):
        product_id = product.get('id', i + 1)
        errors = validate_product(product, product_id)
        
        if errors:
            all_errors.extend(errors)
            print(f"❌ Product {product_id} has {len(errors)} validation error(s):")
            for error in errors:
                print(f"   - {error}")
            print()
        else:
            valid_products += 1
    
    # Summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Total products tested: {len(products)}")
    print(f"Valid products: {valid_products}")
    print(f"Products with defects: {len(products) - valid_products}")
    print(f"Total validation errors: {len(all_errors)}")
    print()
    
    if all_errors:
        print("DEFECTS FOUND:")
        print("-" * 30)
        for error in all_errors:
            print(f"• {error}")
    else:
        print("✅ No defects found! All products passed validation.")
    
    print("=" * 60)


if __name__ == "__main__":
    run_api_tests() 