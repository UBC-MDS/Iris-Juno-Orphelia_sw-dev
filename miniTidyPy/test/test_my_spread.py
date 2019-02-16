# This is a test for the function my_spread
# It creates dataframe to test the function
# and checks if they meet the requirements
# It includes four test functions in total

# import our functions
import os
import sys
sys.path.insert(0, os.path.abspath("../../miniTidyPy"))
import miniTidyPy

# import packages
import pandas as pd
import pytest

# create dataframes for testing

# sample input dataframe
s1 = {'city': ['Vancouver', 'Burnaby', 'Vancouver', 'Richmond'],
      'time': ['morning',  'morning', 'evening', 'evening'],
      'value': [12, 20, 5, 8]}
sample_df = pd.DataFrame(data = s1)

# sample output
s2 = {'city': ['Vancouver', 'Burnaby', 'Richmond'],
      'morning': [12, 20, None],
      'evening': [5, None, 8]}
output1 = pd.DataFrame(data = s2)

# sample input dataframe containing NaN
s_3 = {'city': ['Vancouver', 'Burnaby', 'Vancouver', 'Richmond'],
      'time': ['morning',  'morning', 'evening', float('NaN')],
      'value': [12, 20, 5, 8]}
sample_df_na = pd.DataFrame(data = s_3)

# sample input dataframe with all NaN
all_na = {'a': [None, None],
      'b': [None, None]}
all_na = pd.DataFrame(data = all_na)

# sample output dataframe containing NaN
s_4 = {'city': ['Vancouver', 'Burnaby', 'Richmond'],
      'morning': [12, 20, None],
      'evening': [5, None, None]}
output_na = pd.DataFrame(data = s_4)


# Testing methods

def test_my_spread_normal():
    '''Test on a normal dataframe'''

    # spread the selected column
    d1_test = miniTidyPy.my_spread(sample_df, key = 'time', value = 'value')
    assert d1_test.equals(output1), "normal dataframe"

def test_my_spread_wrong_key():
    '''When the input key is not included, should return the original dataframe'''

    # input is a list
    d2_test = miniTidyPy.my_spread(sample_df, key = [], value = 'value')
    assert d2_test.equals(sample_df), "key is a list"

    # input is an integer
    d3_test = miniTidyPy.my_spread(sample_df, key = 2, value = 'value')
    assert d3_test.equals(sample_df), "key is an integer"

def test_my_spread_wrong_df():
    '''When the input df is not a dataframe, should return None'''

    d4_test = miniTidyPy.my_spread(2, key = 'foo', value = 'foo')
    assert d4_test is None, "input dataframe type incorrect"

def test_my_spread_na():
    '''When key column contains NaN, do not add NaN as a column name'''

    d0_test = miniTidyPy.my_spread(sample_df_na, key = 'time', value = 'value')
    assert d0_test.equals(output_na), "key column contains NaN"

    # when the whole dataframe contains NaN
    with pytest.raises(ValueError):
        miniTidyPy.my_spread(all_na, key = 'a', value = 'b')
