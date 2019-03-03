# Mini Tidy Package for Python - `miniTidyPy`

### Contributors:
- Orphelia Ellogne (`ellognea`)
- Huijue Chen (`huijuechen`)
- Luo Yang (`lyiris22`)


### Summary
For this project we would like to re-implement Python’s melt(), pivot() and dropna() functions to deepen our understanding of them. Our functions would have similar or simpler features compared to these functions. We will give them the following names, respectively.

- `my_gather()` : Transform data frame from wide to long by combining columns. For selected columns, put the columns names into a column of keys, and the values into a column of values.

- `my_spread()`: Separate existing columns into multiple columns.  Select a ‘key’ column whose content will be the names of the new columns. Select a ‘value’ column whose content will be the values of the new columns.

- `my_dropna()` :Remove the entire rows that containing `NA` values from a data frame.

To test our functions, our package will include an additional function that creates a small dataframe with two columns.

Our functions were inspired from the following functions that exist in the Pandas ecosystem:
- [`pandas.melt`](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html)
- [`pandas.DataFrame.pivot`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html)
- [`pandas.DataFrame.dropna`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)

### Installation

`miniTidyPy` can be installed with pip from Github using:
- `pip install git+https://github.com/UBC-MDS/mini_tidy_python.git`

### Example Usage

We would use the below dataset as an example and apply the 3 functions above step by step. Also the complete working file with this dataset can be found [here](doc/ToyDataExampleUsage.ipynb).

```
import pandas as pd
import miniTidyPy as mt

sample_df = pd.DataFrame({'city': ['Vancouver', 'Burnaby', 'Richmond'], 'morning': [12, 20, 15], 'evening': [5, 8 ,3], 'midnight' : [-1,2, None]})
sample_df
```

| city | morning	 | evening| midnight|
|---|---|--|--|
| Vancouver | 12 |5|-1.0|
| Burnaby | 20 |8|2.0|
| Richmond | 15 |3|NaN|

After applying `my_dropna` to remove the rows containing `NA` values, we get below:

```
dropna_df = mt.my_dropna(sample_df)
dropna_df
```

| city | morning	 | evening| midnight|
|---|---|--|--|
| Vancouver | 12 |5|-1.0|
| Burnaby | 20 |8|2.0|

After applying `my_gather` to remove the rows containing `NA` values, we get below:

```
gather_df = mt.my_gather(dropna_df, keyname = 'time', valuename = 'value', keys = ['morning','evening', 'midnight'])
gather_df
```

| city | key	 | value|
|---|---|--|
| Vancouver | morning |12.0|
| Burnaby | morning|20.0|
| Vancouver | evening |5.0|
| Burnaby | evening|8.0|
| Vancouver | midnight |-1.0|
| Burnaby | midnight|2.0|

After applying `my_spread` to separate existing columns into multiple columns, we get below:

```
spread_df = mt.my_spread(gather_df, key = 'time', value = 'value')
spread_df
```

| city | morning	 | evening| midnight|
|---|---|--|--|
| Vancouver | 12 |5|-1.0|
| Burnaby | 20 |8|2.0|

### Control Flow Diagram

The control flow diagrams can be found in the links if interested: [`my_dropna`](doc/control_flow_my_dropna.png), [`my_gather`](doc/control_flow_my_gather.png), and [`my_spread`](doc/control_flow_my_spread.png).

### Branch Coverage

To test branch coverage, we use [coverage.py](https://coverage.readthedocs.io/en/coverage-4.2/index.html#). It can be installed with `pip install coverage`.

We run below on a local directory of the package repo to obtain the coverage [result](doc/branch_coverage_result.png):
- `coverage run -m --branch pytest -q miniTidyPy/test/test_my_dropna.py miniTidyPy/test/test_my_gather.py miniTidyPy/test/test_my_spread.py`

```
Name                                Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------------------
miniTidyPy/__init__.py                  4      0      0      0   100%
miniTidyPy/my_dropna.py                17      0     10      0   100%
miniTidyPy/my_gather.py                32      0     22      0   100%
miniTidyPy/my_spread.py                51      0     38      0   100%
miniTidyPy/test/__init__.py             0      0      0      0   100%
miniTidyPy/test/test_my_dropna.py      18      0      0      0   100%
miniTidyPy/test/test_my_gather.py      46      0      0      0   100%
miniTidyPy/test/test_my_spread.py      34      0      0      0   100%
-------------------------------------------------------------------------------
TOTAL                                 202      0     70      0   100%
```

### Important files(in update)
* README.md
* [Testing Units Design](miniTidyPy/test/):
  + testing units for `my_dropna`: [test_my_dropna.py](miniTidyPy/test/test_my_dropna.py)
  + testing units for `my_gather`: [test_my_gather.py](miniTidyPy/test/test_my_gather.py)
  + testing units for `my_spread`: [test_my_spread.py](miniTidyPy/test/test_my_spread.py)
