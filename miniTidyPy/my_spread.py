# This is the script for function my_spread

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

    # check if input is a dataframe
    if not isinstance(df, pd.DataFrame):
        return None

    # check if key and value are in list(df)
    if key not in list(df):
        return df
    if value not in list(df):
        return df


    # build a structure for the new dataframe
    struc = {} # dictionary to build the dataframe
    preserved = [] # list containing the column names not selected as keys

    # get the unique values in the key column
    keys = []
    for i in df[key]:
        if i not in keys and not pd.isnull(i):
            keys.append(i)

    added = False # check if the new key and value columns had been added
    for col in list(df):
        if col != key and col != value: # the preserved columns
            struc[col] = []
            preserved.append(col)
            
    # if no preserved columns, raise an error
    if len(preserved) == 0:
        raise ValueError('Dataframe without unique identifiers')

    # add key columns and value to the end
    for keyname in keys:
        struc[keyname] = []
        
    # check if the preserved columns and the key columns form unique identifiers
    check_id = []
    for i in range(df.shape[0]):
        idf = ""
        for col in preserved:  # add preserved column value to the string
            idf = idf + str(df[col][i]) + " "
        idf = idf + str(df[key][i]) # add key column value to the string
        check_id.append(idf)
    if len(check_id) != len(set(check_id)):
        raise ValueError('Dataframe without unique identifiers')

    # turn the values in the preserved columns into a list of strings
    pre_combos = []
    for i in range(df.shape[0]):
        combo = []
        for col in preserved:
            combo.append(df[col][i])
        pre_combos.append(combo)

    # build a dictionary for the preserved columns
    combo_dic = {}
    for combo in pre_combos:
        row_dic = {}
        for i in range(len(preserved)):
            row_dic[preserved[i]] = combo[i]

        for keyname in keys:
            row_dic[keyname] = None

        combo_dic[str(combo)] = row_dic

    # add the values to the row dictionary
    for i in range(df.shape[0]):
        combo_name = str(pre_combos[i])
        combo_dic[combo_name][df[key][i]] = df[value][i]

    # add the new rows to the dataframe
    for c in list(combo_dic):
        for colname in list(struc):
            struc[colname].append(combo_dic[c][colname])

    return pd.DataFrame(struc) 