import pytest
import math 

@pytest.fixture
def sampleData():
    print("\nSetting up sampleData...")
    data = [1, 2, 3]
    yield data
    print("Tearing down sampleData...")

def test_sum_of_sampleData(sampleData):
    print(f"Inside test_sum_of_sampleData: {sampleData}")
    assert sum(sampleData) == 6, f"Expected sum of {sampleData} to be 6, but got {sum(sampleData)}"

def test_product_of_sampleData(sampleData):
    print(f"Inside test_product_of_sampleData: {sampleData}")
    product = math.prod(sampleData)
    assert product == 6, f"Expected product of {sampleData} to be 6, but got {product}"