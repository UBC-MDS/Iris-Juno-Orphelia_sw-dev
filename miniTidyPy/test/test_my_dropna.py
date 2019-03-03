
# Feb 2019
# This script contains tests for the my_dropna function
# The function creates a new dataframe by removing the rows with "NaN" values in the original dataframe
# input: dataframe
# output: dataframe
#------------------------------------
# Import our functions
import os
import sys
sys.path.insert(0, os.path.abspath("../../miniTidyPy"))
import miniTidyPy
#------------------------------------
# Required packages
import pandas as pd
import pytest
#------------------------------------
# Create dataframes for testing
# test input
empty_df = pd.DataFrame()
input_df = pd.DataFrame({"A":[25,15,None,30], "y": [0,1,0, None], "z": ["Yes", "No", "Yes", "No"]})
# test output
output_df = input_df.dropna()
#------------------------------------
# Testing Functions

def test_my_dropna_empty():
    '''Test empty dataframe'''
    d1_test = miniTidyPy.my_dropna(empty_df)
    assert d1_test.equals(empty_df), "empty dataframe, output with empty dataframe"

def test_my_dropna_normal():
    '''Test normal dataframe'''
    d2_test = miniTidyPy.my_dropna(input_df)
    assert d2_test.equals(output_df), "normal dataframe, rows with NAs removed"

def test_my_dropna_wrong_input():
    '''When the input data is not a dataframe, return error message'''
    # input is not a dataframe, should return None and display error message
    with pytest.raises(TypeError):
            miniTidyPy.my_dropna([1,2,3])
