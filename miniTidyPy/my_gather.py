# This script defines the function my_gather

# Required packages
# Note that mypy does not work with python module
import pandas as pd

# Define function
def my_gather(df: pd.core.frame.DataFrame, keys: list, keyname: str = 'key', valuename: str = 'value') -> pd.core.frame.DataFrame:
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

    # raise error for wrong type of input
    if not isinstance(df, pd.DataFrame):
        raise ValueError('Input data must be pandas dataframe')
    if not isinstance(keys, list):
        raise ValueError('Input keys must be a list')
    if not isinstance(keyname, str):
        raise ValueError('Input keyname must be a string')
    if not isinstance(valuename, str):
        raise ValueError('Input valuename must be a string')

    # build a structure for the new dataframe
    struc: dict = {} # dictionary to build the dataframe
    preserved = [] # list containing the column names not selected as keys
    truekeys = [] # list containing the actual useful column names

    added = False # check if the new key and value columns had been added
    for col in list(df):
        if col not in keys: # the preserved columns
            struc[col] = []
            preserved.append(col)
        else:
            truekeys.append(col)
            if added == False:
                struc[keyname] = []
                struc[valuename] = []
                added = True

    # if no correct keys, return the original dataframe
    if truekeys == []:
        return df

    # add the data to the structure of the new dataframe
    for key in truekeys:
        for i in range(df.shape[0]):
            struc[keyname].append(key)
            struc[valuename].append(df[key][i])
            for precol in preserved:
                struc[precol].append(df[precol][i])

    return pd.DataFrame(struc)