# Pandas sublcass with additional helper methods

## Install
```
pip install -i https://test.pypi.org/simple/ lambdata-richmondtest
```

## Helper Methods:
### Tabulate
Format the dataframe table for pretty printing. This is a wrapper method for https://pypi.org/project/tabulate/
It checks for `display.max_rows` and `display.max_columns` and uses them by default for generating the output table.


#### Example Usage: 
```python
>>> from lambdata_richmondtest import DataFrameWithHelpers
>>> from faker import Faker
>>> import pandas as pd
>>> import datetime
>>> fake = Faker()
>>> pd.set_option('display.max_rows', 20)
>>> #Create a DataFrame from random dates
>>> start_date = datetime.date(year=2010, month=1, day=1)
>>> end_date = datetime.date(year=2020, month=1, day=1)
>>> fake_dates = [fake.date_between(start_date=start_date, end_date=end_date) for x in range(1000)]
>>> df = DataFrameWithHelpers(fake_dates,columns=['Date'])
>>> print(df.tabulate())
```
```
---  ----------
0    2017-10-21
1    2017-11-09
2    2017-03-12
3    2016-10-28
4    2013-12-29
5    2018-08-25
6    2012-01-19
7    2015-03-12
8    2011-08-21
9    2010-04-01
...  ...
990  2010-10-23
991  2017-03-30
992  2014-03-11
993  2013-02-18
994  2019-10-12
995  2018-11-05
996  2012-06-22
997  2010-05-30
998  2019-12-11
999  2017-08-04
---  ----------
```
##### Github Flavored Markdown:

```python
>>> print(df.tabulate(headers='keys', tablefmt="github",))
```
```
|     | Date       |
|-----|------------|
| 0   | 2017-10-21 |
| 1   | 2017-11-09 |
| 2   | 2017-03-12 |
| 3   | 2016-10-28 |
| 4   | 2013-12-29 |
| 5   | 2018-08-25 |
| 6   | 2012-01-19 |
| 7   | 2015-03-12 |
| 8   | 2011-08-21 |
| 9   | 2010-04-01 |
| ... | ...        |
| 990 | 2010-10-23 |
| 991 | 2017-03-30 |
| 992 | 2014-03-11 |
| 993 | 2013-02-18 |
| 994 | 2019-10-12 |
| 995 | 2018-11-05 |
| 996 | 2012-06-22 |
| 997 | 2010-05-30 |
| 998 | 2019-12-11 |
| 999 | 2017-08-04 |
```

##### HTML:

```python

>>> print(df.tabulate(headers='keys', tablefmt="html",))

```




```html
<table>
<thead>
<tr><th>   </th><th>Date      </th></tr>
</thead>
<tbody>
<tr><td>0  </td><td>2017-10-21</td></tr>
<tr><td>1  </td><td>2017-11-09</td></tr>
<tr><td>2  </td><td>2017-03-12</td></tr>
<tr><td>3  </td><td>2016-10-28</td></tr>
<tr><td>4  </td><td>2013-12-29</td></tr>
<tr><td>5  </td><td>2018-08-25</td></tr>
<tr><td>6  </td><td>2012-01-19</td></tr>
<tr><td>7  </td><td>2015-03-12</td></tr>
<tr><td>8  </td><td>2011-08-21</td></tr>
<tr><td>9  </td><td>2010-04-01</td></tr>
<tr><td>...</td><td>...       </td></tr>
<tr><td>990</td><td>2010-10-23</td></tr>
<tr><td>991</td><td>2017-03-30</td></tr>
<tr><td>992</td><td>2014-03-11</td></tr>
<tr><td>993</td><td>2013-02-18</td></tr>
<tr><td>994</td><td>2019-10-12</td></tr>
<tr><td>995</td><td>2018-11-05</td></tr>
<tr><td>996</td><td>2012-06-22</td></tr>
<tr><td>997</td><td>2010-05-30</td></tr>
<tr><td>998</td><td>2019-12-11</td></tr>
<tr><td>999</td><td>2017-08-04</td></tr>
</tbody>
</table>
```
Check out: https://pypi.org/project/tabulate/ for formats and faeatures documentation.

### train_test_val_split
Split the data frame into random train, test and val subsets.
Uses [sklearn.model_selection.train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) to split the data into train/test then splits train furtuer to train/val
#### Example Usage: 

```python
>>> train, test, val = df.train_test_val_split()
>>> print(train.shape, test.shape, val.shape)
(562, 1) (250, 1) (188, 1)
```
Compatible with [**train_test_split**](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)'s parameters 
```python
>>> train, test, val = df.train_test_val_split(test_size=0.30)
>>> print(train.shape, test.shape, val.shape)
(490, 1) (300, 1) (210, 1)
```
### split_dates
 Split a date column into multiple columns for day, month and year.
 ```python
 df.split_dates('Date')
 ```
|     | Date       | day   | month   | year   |
|-----|------------|-------|---------|--------|
| 0   | 2018-08-28 | 28    | 8       | 2018   |
| 1   | 2013-08-23 | 23    | 8       | 2013   |
| 2   | 2011-05-21 | 21    | 5       | 2011   |
| 3   | 2011-03-01 | 1     | 3       | 2011   |
| 4   | 2014-09-29 | 29    | 9       | 2014   |
| 5   | 2018-05-13 | 13    | 5       | 2018   |
| 6   | 2010-05-15 | 15    | 5       | 2010   |
| 7   | 2015-12-27 | 27    | 12      | 2015   |
| 8   | 2011-06-13 | 13    | 6       | 2011   |
| 9   | 2018-05-15 | 15    | 5       | 2018   |
| ... | ...        | ...   | ...     | ...    |
| 990 | 2017-08-02 | 2     | 8       | 2017   |
| 991 | 2010-10-31 | 31    | 10      | 2010   |
| 992 | 2012-02-25 | 25    | 2       | 2012   |
| 993 | 2010-08-29 | 29    | 8       | 2010   |
| 994 | 2014-09-11 | 11    | 9       | 2014   |
| 995 | 2018-08-18 | 18    | 8       | 2018   |
| 996 | 2019-09-02 | 2     | 9       | 2019   |
| 997 | 2011-10-07 | 7     | 10      | 2011   |
| 998 | 2010-01-11 | 11    | 1       | 2010   |
| 999 | 2018-12-05 | 5     | 12      | 2018   |

With custom prefix:
 ```python
 df.split_dates('Date', prefix='date_')
 ```
|     | Date       | date_day   | date_month   | date_year   |
|-----|------------|------------|--------------|-------------|
| 0   | 2018-11-28 | 28         | 11           | 2018        |
| 1   | 2012-10-14 | 14         | 10           | 2012        |
| 2   | 2019-04-22 | 22         | 4            | 2019        |
| 3   | 2015-08-03 | 3          | 8            | 2015        |
| 4   | 2011-11-28 | 28         | 11           | 2011        |
| 5   | 2016-01-15 | 15         | 1            | 2016        |
| 6   | 2018-02-01 | 1          | 2            | 2018        |
| 7   | 2019-08-07 | 7          | 8            | 2019        |
| 8   | 2010-10-07 | 7          | 10           | 2010        |
| 9   | 2019-10-07 | 7          | 10           | 2019        |
| ... | ...        | ...        | ...          | ...         |
| 990 | 2017-12-19 | 19         | 12           | 2017        |
| 991 | 2016-10-27 | 27         | 10           | 2016        |
| 992 | 2010-10-31 | 31         | 10           | 2010        |
| 993 | 2013-05-02 | 2          | 5            | 2013        |
| 994 | 2019-07-04 | 4          | 7            | 2019        |
| 995 | 2014-03-23 | 23         | 3            | 2014        |
| 996 | 2012-05-23 | 23         | 5            | 2012        |
| 997 | 2014-09-12 | 12         | 9            | 2014        |
| 998 | 2018-03-18 | 18         | 3            | 2018        |
| 999 | 2013-10-02 | 2          | 10           | 2013        |