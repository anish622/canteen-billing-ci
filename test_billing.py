import pytest
from billing import calculate_total


def test_gst_only_below_threshold():
    assert calculate_total([(100, 1)]) == 105.0


def test_no_discount_at_exactly_300():
    assert calculate_total([(150, 2)]) == 315.0


def test_discount_above_300():
    assert calculate_total([(200, 2)]) == 378.0


def test_multiple_items_with_discount():
    assert calculate_total([(120, 2), (80, 1)]) == 302.4


def test_empty_order():
    assert calculate_total([]) == 0.0


def test_negative_price_rejected():
    with pytest.raises(ValueError):
        calculate_total([(-50, 1)])