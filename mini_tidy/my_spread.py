# This is the script for function my_spread 
# Function left black at this point for further contributions

# import packages
import pandas as pd

# function
def my_spread(df, key, value):
    '''
    Separate existing columns into multiple columns
    Select one 'key' column whose content will be the names of the new columns
    Select one 'value' column whose content will the values of the new columns


    Args:
        df (dataframe): a pandas dataframe to be transformed
        keys (string): column name selected to be the 'key'
        valuename (string): column name selected to be the 'value'

    Returns:
        new_df (dataframe): the transformed new dataframe
    '''
