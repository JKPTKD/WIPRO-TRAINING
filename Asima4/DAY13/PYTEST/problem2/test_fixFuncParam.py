import pytest
import math

def test_sum_with_param_fixture_function(sumDataFix):
    data_list, expected_sum = sumDataFix
    print(f"\n[test_fixFuncParam.py] Test parameterized sum data: {data_list}")
    assert sum(data_list) == expected_sum, f"Expected sum {expected_sum}, got {sum(data_list)}"

def test_product_with_param_fixture_function(prodDataFix):
    data_list, expected_product = prodDataFix
    print(f"\n[test_fixFuncParam.py] Test parameterized product data: {data_list}")
    assert math.prod(data_list) == expected_product, f"Expected product {expected_product}, got {math.prod(data_list)}"