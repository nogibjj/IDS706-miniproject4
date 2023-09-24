"""
This is the main module of the project.
"""
import numpy as np


def add_arrays(arr1, arr2):
    """
    Adds two numpy arrays element-wise.

    Parameters:
        arr1 (numpy.ndarray): First input array.
        arr2 (numpy.ndarray): Second input array.

    Returns:
        numpy.ndarray: Resultant array after element-wise addition.
    """
    return arr1 + arr2


def multiply_dataframe_column(df, column_name, factor):
    """
    Multiplies a column in a pandas DataFrame by a specified factor.

    Parameters:
        df (pandas.DataFrame): Input DataFrame.
        column_name (str): Name of the column to be multiplied.
        factor (float): Factor by which to multiply the column.

    Returns:
        pandas.DataFrame: Resultant DataFrame with the modified column.
    """
    df[column_name] = df[column_name] * factor
    return df


def calculate_mean_of_positive_elements(arr):
    """
    Calculates the mean of positive elements in a numpy array.

    Parameters:
        arr (numpy.ndarray): Input array.

    Returns:
        float: Mean of positive elements in the array.
    """
    positive_elements = arr[arr > 0]
    return np.mean(positive_elements)
