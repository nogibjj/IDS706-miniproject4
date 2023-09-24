"""
This file contains unit tests for the functions in main.py.
"""
import numpy as np
import pandas as pd
from main import (
    add_arrays,
    multiply_dataframe_column,
    calculate_mean_of_positive_elements,
)


def test_add_arrays():
    """
    Test that the add_arrays function adds two arrays correctly.
    """
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    result = add_arrays(arr1, arr2)
    expected_result = np.array([5, 7, 9])
    np.testing.assert_array_equal(result, expected_result)


def test_multiply_dataframe_column():
    """
    Test that the multiply_dataframe_column function multiplies a column in a DataFrame by a factor correctly.
    """
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    column_name = "B"
    factor = 2
    result = multiply_dataframe_column(df, column_name, factor)
    expected_result = pd.DataFrame({"A": [1, 2, 3], "B": [8, 10, 12]})
    pd.testing.assert_frame_equal(result, expected_result)


def test_calculate_mean_of_positive_elements():
    """
    Test that the calculate_mean_of_positive_elements function calculates the mean of positive elements in an array correctly.
    """
    arr = np.array([-1, 2, 3, -4, 5])
    result = calculate_mean_of_positive_elements(arr)
    expected_result = 3.3333333333333335
    assert np.isclose(result, expected_result)
