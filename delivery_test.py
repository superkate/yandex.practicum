from calculate_delivery_cost import *

import pytest

testdata = [
    (1.5, True, True, "very high", 880),
    (2, False, True, "high", 630),
    (8, False, True, "increased", 600),
    (10, True, True, "", 600),
    (20, True, False, "very high", 640),
    (30, False, True, "high", 840),
    (100, True, False, "increased", 600)
]

@pytest.mark.parametrize("distance, is_big, is_fragile, delivery_load, expected_cost", testdata)
def test_calculate_delivery_cost(distance, is_big, is_fragile, delivery_load, expected_cost):
    assert calculate_delivery_cost(distance, is_big, is_fragile, delivery_load) == expected_cost

def test_calculate_delivery_cost_returns_minimum_delivery_cost_if_calculated_cost_is_less_than_minimal():
    assert calculate_delivery_cost(1, False, False) == 400

def test_calculate_delivery_cost_for_fragile_package_and_distance_longer_than_allowed_maximum():
    with pytest.raises(TooLongDistanceForFragilePackageException):
        calculate_delivery_cost(100, False, True)

def test_calculate_delivery_cost_for_distance_less_than_zero():
    with pytest.raises(DistanceIsLessThanOrEqualToZeroException):
        calculate_delivery_cost(-1, False, False)

def test_calculate_delivery_cost_for_distance_equal_to_zero():
    with pytest.raises(DistanceIsLessThanOrEqualToZeroException):
        calculate_delivery_cost(0, False, False)
