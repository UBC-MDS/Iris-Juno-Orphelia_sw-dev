# February 2019
# This script defines the function my_dropna.py
# The function creates a new dataframe by removing the rows with "NaN" values in the original dataframe
#------------------------------------
# Required packages
import pandas as pd
#------------------------------------
# Define function
def my_dropna(df, key, value):
    '''
        If the input is dataframe, check through the dataframe and remove the rows with NaN values.

        Parameters
        ----------
        param1 : dataframe
            A dataframe to remove the rows with NaN values.

        Returns
        -------
        Dataframe
        The output will be a dataframe with the entire rows with NA values removed from the input dataframe.
    '''
