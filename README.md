# Mini Tidy Package for Python

### Contributors:
- Orphelia Ellogne (`ellognea`)
- Huijue Chen (`huijuechen`)
- Luo Yang (`lyiris22`)


### Summary
For this project we would like to re-implement Python’s melt(), pivot() and dropna() functions to deepen our understanding of them. Our functions would have similar or simpler features compared to these functions. We will give them the following names, respectively.

- `my_gather()` : Make data from wide to long by combining columns. For selected columns, put the columns names into a column of keys, and the values into a column of values.

- `my_spread()`: Separate existing columns into multiple columns.  Select a ‘key’ column whose content will be the names of the new columns. Select a ‘value’ column whose content will be the values of the new columns.

- `my_dropna()` : Remove NAs from a dataframe.

To test our functions, our package will include an additonal function that creates a small dataframe with two columns. 

Our functions were inspired from the following functions that exist in the Pandas ecosystem:
- [`pandas.melt`](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html)
- [`pandas.DataFrame.pivot`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html)
- [`pandas.DataFrame.dropna`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)

