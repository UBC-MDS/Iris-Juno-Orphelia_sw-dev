
# Feb 2019
# This script contains tests for the my_dropna function
# The function creates a new dataframe by removing the rows with NA values in the original dataframe
# input: dataframe
# output: dataframe
#------------------------------------
# Required packages
import pandas as pd
import pytest
#------------------------------------

# create dataframes for testing

# test input
s1 = {'A': [25, 15, 30, NA], 'B': [0, 1, NA, 1], 'C': ["Yes", "No", "Yes", "No"]}
input_df = pd.DataFrame(data = s1)

# test output
s2 = {'A': [25, 15], 'B': [0, 1], 'C': ["Yes", "No"]}
output_df = pd.DataFrame(data = s2)

# Testing methods

def test_my_dropna_normal():
    '''Test with normal inputs'''

    d1_test = my_dropna(input_df)
    assert d1_test.equals(output_df), "normal dataframe, rows with NAs removed"

def test_my_dropna_wrong_input():
    '''When the type of input data is not dataframe, should return None'''

    # input is not a dataframe, should return None and display error message
    d7_test = my_dropna([1,2,3])
    assert d7_test is None, "Error: Expect input to be a dataframe"
