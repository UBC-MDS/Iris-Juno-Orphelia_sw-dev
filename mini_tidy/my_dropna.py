# February 2019
# this script tests the function for my_dropna.py
# this function removes the rows in a datafram that containing "NA"

# Required packages
import pandas as pd

# function
def my_spread(df, key, value):
    '''
        If the input is dataframe, check through the dataframe and remove the rows with NA values.

        Parameters
        ----------
        param1 : dataframe
            A dataframe to remove the rows with NA values.

        Returns
        -------
        Dataframe
        The output will be a dataframe with the entire rows with NA values removed from the input dataframe.
    '''
