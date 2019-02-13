
# Feb 2019
# This script contains tests for the my_dropna function
# The function creates a new dataframe by removing the rows with "NaN" values in the original dataframe
# input: dataframe
# output: dataframe
#------------------------------------
# Required packages
import pandas as pd
import pytest
#------------------------------------

# create dataframes for testing

# test input
input_df = pd.DataFrame({"A":[25,15,None,30], "y": [0,1,0, None], "z": ["Yes", "No", "Yes", "No"]})

# test output
output_df = input_df.dropna()

# Testing methods

def test_my_dropna_normal():
    '''Test normal dataframe'''

    d1_test = my_dropna(input_df)
    assert d1_test.equals(output_df), "normal dataframe, rows with NAs removed"

def test_my_dropna_wrong_input():
    '''When the input data is not a dataframe, return error message'''

    # input is not a dataframe, should return None and display error message
    d7_test = my_dropna([1,2,3])
    assert d7_test is None, "Error: Expect input to be a dataframe"
