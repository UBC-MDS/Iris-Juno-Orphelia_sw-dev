# documentation

# import packages
import pandas as pd

# function
def my_gather(df, keys, valuename = 'value'):
    '''
    Make dataframe from wide to long by combining columns
    For the selected columns, put the column names into a new column 'keys'
    and the values into a new column 'values'

    Args:
        df (dataframe): a pandas dataframe to be transformed
        keys (list of strings): columns names to be put in the 'key' column
        valuename (string): name for the new 'value' column

    Returns:
        new_df (dataframe): the transformed new dataframe
    '''
