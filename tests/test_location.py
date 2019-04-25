"""Tests for the location mystats.eda.module"""

import pytest
from mystats.eda import location

def test_mean_empty_dataset_returns_none():
    result = location.mean([])

    assert result is None

def test_mean_none_dataset_throws_value_error():
    with pytest.raises(ValueError):
        location.mean(None)

def test_mean_integer_values_noninteger_result():
    result = location.mean([1,2])

    assert result == pytest.approx(1.5, 0.01)

def test_mean_data_and_weights_have_different_lengths_raise_value_error():
    with pytest.raises(ValueError):
        location.mean(data=[1,2,3], weights=[1,2])

def test_mean_correctly_calculates_weighted_mean():
    result = location.mean(data=[92,68,81], weights=[10,20,70])

    assert result == pytest.approx(79.5, 0.01)

def test_mean_trimmed_zero_same_as_untrimmed():
    result = location.mean(data=[92,68,81], trimmed=0)
    result2 = location.mean(data=[92,68,81])

    assert result == result2

def test_mean_sorted_correctly_calculated_trimmed_mean():
    result = location.mean(data=[0,50,60,100], trimmed=1)

    assert result == 55

def test_mean_unsorted_correctly_calculated_trimmed_mean():
    result = location.mean(data=[60,100,0,50], trimmed=1)

    assert result == 55