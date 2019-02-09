# documentation

# import packages
import pandas as pd
import pytest

# create dataframes for testing

# sample dataframe input
s1 = {'city': ['Vancouver', 'Burnaby'], 'morning': [12, 20], 'evening': [5, 8], 'midnight' : [-1, None]}
sample_df = pd.DataFrame(data = s1)

# sample output 1
s2 = {'city': ['Vancouver', 'Burnaby', 'Vancouver', 'Burnaby'],
      'time': ['morning',  'morning', 'evening', 'evening'],
      'value': [12, 20, 5, 8],
      'midnight' : [-1, None, -1, None]}
output1 = pd.DataFrame(data = s2)

# sample output 2
s3 = {'city': ['Vancouver', 'Burnaby', 'Vancouver', 'Burnaby', 'Vancouver', 'Burnaby'],
      'time': ['morning',  'morning', 'evening', 'evening', 'midnight', 'midnight'],
      'value': [12, 20, 5, 8, -1, None]}
output2 = pd.DataFrame(data = s3)

# Testing methods

def test_my_gather_normal():
    '''Test with normal inputs'''

    # gather two columns
    d1_test = my_gather(sample_df, keys = ['morning','evening'], valuename = 'value')
    assert d1_test.equals(output1), "normal dataframe, gather two"

    # gather three columns
    d2_test = my_gather(sample_df, keys = ['morning','evening','midnight'], valuename = 'value')
    assert d2_test.equals(output2), "normal dataframe, gather three"

def test_my_gather_wrong_list():
    '''When the input list is incorrect, should return the original dataframe'''

    # wrong column input, should return the original dataframe
    d3_test = my_gather(sample_df, keys = ['foo'], valuename = 'value')
    assert d3_test.equals(sample_df), "one wrong column name"

    # empty string should return the original dataframe
    d4_test = my_gather(sample_df, keys = [], valuename = 'value')
    assert d4_test.equals(sample_df), "empty list of column names"

def test_my_gather_wrong_extra():
    '''When the input list is partially wrong, should ignore the extra entries'''

    # extra column name that does not exist, should ignore it
    d5_test = my_gather(sample_df, keys = ['morning','evening','foo'], valuename = 'value')
    assert d5_test.equals(output1), "extra wrong column names"

    # extra entry in the list that is not a string, should ignore it
    d6_test = my_gather(sample_df, keys = ['morning','evening',2], valuename = 'value')
    assert d6_test.equals(output1), "extra wrong type in the string"

def test_my_gather_wrong_df():
    '''When the input dataframe is incorrect, should return None'''

    # input is not a dataframe, should return None
    d7_test = my_gather(2, keys = ['foo'], valuename = 'value')
    assert d7_test is None, "input dataframe type incorrect"

    # keys is not a list, should return the original dataframe
    d8_test = my_gather(sample_df, keys = 2, valuename = 'value')
    assert d8_test.equals(sample_df), "input keys(name) type incorrect"
