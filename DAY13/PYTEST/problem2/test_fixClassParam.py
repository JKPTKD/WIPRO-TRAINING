import pytest
import math

class TestParameterizedListOperations:

    def test_sum_in_class_with_params(self, sumDataFix):
        data_list, expected_sum = sumDataFix
        print(f"\n[test_fixClassParam.py] Test parameterized sum data in class: {data_list}")
        assert sum(data_list) == expected_sum, f"Expected sum {expected_sum}, got {sum(data_list)}"

    def test_product_in_class_with_params(self, prodDataFix):
        data_list, expected_product = prodDataFix
        print(f"\n[test_fixClassParam.py] Test parameterized product data in class: {data_list}")
        assert math.prod(data_list) == expected_product, f"Expected product {expected_product}, got {math.prod(data_list)}"