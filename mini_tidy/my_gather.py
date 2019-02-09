# This is the script for function my_spread
# Function left black at this point for further contributions

# import packages
import pandas as pd

# function
def my_gather(df, keyname = 'key', valuename = 'value', keys):
    '''
    Make dataframe from wide to long by combining columns
    For the selected columns, put the column names into a new column 'keys'
    and the values into a new column 'values'

    Args:
        df (dataframe): a pandas dataframe to be transformed
        keyname (string): name for the new 'key' column
        valuename (string): name for the new 'value' column
        keys (list of strings): columns names to be put in the 'key' column

    Returns:
        new_df (dataframe): the transformed new dataframe
    '''
