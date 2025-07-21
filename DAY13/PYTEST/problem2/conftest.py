import pytest
import math

@pytest.fixture
def sumData():
    print("\n[conftest.py] Setting up sumData...")
    data = [1, 2, 3]
    expected_result = 6
    yield data, expected_result
    print("[conftest.py] Tearing down sumData...")

@pytest.fixture
def prodData():
    print("\n[conftest.py] Setting up prodData...")
    data = [1, 2, 3]
    expected_result = 6
    yield data, expected_result
    print("[conftest.py] Tearing down prodData...")

@pytest.fixture(params=[
    ([1, 2, 3], 6),
    ([10, 20], 30),
    ([-1, 0, 1], 0)
], ids=["sum_1_2_3", "sum_10_20", "sum_neg_0_pos"])
def sumDataFix(request):
    data, expected_result = request.param
    print(f"\n[conftest.py] Setting up sumDataFix with data: {data}")
    yield data, expected_result
    print(f"[conftest.py] Tearing down sumDataFix for data: {data}")

@pytest.fixture(params=[
    ([1, 2, 3], 6),
    ([2, 5], 10),
    ([-1, -1, 1], 1)
], ids=["prod_1_2_3", "prod_2_5", "prod_neg_neg_pos"])
def prodDataFix(request):
    data, expected_result = request.param
    print(f"\n[conftest.py] Setting up prodDataFix with data: {data}")
    yield data, expected_result
    print(f"[conftest.py] Tearing down prodDataFix for data: {data}")