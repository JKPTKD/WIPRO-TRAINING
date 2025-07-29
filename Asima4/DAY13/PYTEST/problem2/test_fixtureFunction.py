import pytest 

def test_sum_with_fixture_function(sumData):
    data_list, expected_sum = sumData
    print(f"\n[test_fixtureFunction.py] Test sum data: {data_list}")
    assert sum(data_list) == expected_sum, f"Expected sum {expected_sum}, got {sum(data_list)}"

def test_product_with_fixture_function(prodData):
    data_list, expected_product = prodData
    print(f"\n[test_fixtureFunction.py] Test product data: {data_list}")
    import math 
    assert math.prod(data_list) == expected_product, f"Expected product {expected_product}, got {math.prod(data_list)}"