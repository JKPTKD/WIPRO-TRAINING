import pytest
import math

class TestListOperations:

    def test_sum_in_class(self, sumData):
        data_list, expected_sum = sumData
        print(f"\n[test_fixtureClass.py] Test sum data in class: {data_list}")
        assert sum(data_list) == expected_sum, f"Expected sum {expected_sum}, got {sum(data_list)}"

    def test_product_in_class(self, prodData):
        data_list, expected_product = prodData
        print(f"\n[test_fixtureClass.py] Test product data in class: {data_list}")
        assert math.prod(data_list) == expected_product, f"Expected product {expected_product}, got {math.prod(data_list)}"