"""
Helper Module Containing Helper Functions and a Pandas subclass
with helper methods for some common procedures
"""

from typing import Tuple, Iterable, Union
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import confusion_matrix
from matplotlib.axes import Axes
from tabulate import tabulate
class DataFrameWithHelpers(pd.DataFrame):

    """
    pandas DataFrame with added helper methods for some common procedures
    """

    def train_test_val_split(self, **options) -> Tuple[
            'DataFrameWithHelpers', 'DataFrameWithHelpers', 'DataFrameWithHelpers']:
        """
        Split the dataframe into random train, test and validation subsets.

        It uses sklearn.model_selection.train_test_split to split to train/test,
        and splits the test further to test/validation
        See: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html 
        for parameters options

        """  # noqa
        train, test = train_test_split(self, **options)
        train, val = train_test_split(train, **options)
        return (train, test, val)

    def split_dates(self, column: str, prefix: str = '')\
            -> 'DataFrameWithHelpers':
        """
        Split a date column into multiple columns for day, month and year

        Parameters
        ----------

        :param str column: The date column to use as source
        :param str prefix: The prefix string for the resulting new columns
        :return: A new DataFrame with columns for day, month and year
        :rtype: DataFrameWithHelpers

        """
        date = pd.to_datetime(self[column]).dt
        day = date.day
        month = date.month
        year = date.year
        new_df = self.copy()
        new_df[prefix + 'day'] = day
        new_df[prefix + 'month'] = month
        new_df[prefix + 'year'] = year
        return new_df

    def tabulate(self,
                 headers: Union[str, Iterable] = (),
                 max_rows: int = 0,
                 max_cols: int = 0,
                 **options) -> str:
        """
        Format the dataframe table for pretty printing. This is just
        a wrapper method for https://pypi.org/project/tabulate/

        Parameters
        ----------

        :param list or str headers:
        :param str prefix: List of column headers or the keywords 'firstrow'
        or 'keys'.
        :param int max_rows: Maximum number of rows to print.
        :param int max_cols: Maximum number of cols to print.
        :return: A new DataFrame with columns for day, month and year
        :rtype: DataFrameWithHelpers
        """
        data = self
        if headers == 'keys':
            headers = self.keys()
        
        elif headers == 'firstrow':
            headers = self.iloc[0].values
            data = self.iloc[1:]
            
        row_count, col_count = self.shape
        display_row_count = max_rows or pd.get_option(
                "display.max_rows") or 999999
        display_col_count = max_cols or pd.get_option(
            "display.max_columns") or 999999

        if display_row_count < row_count:
            half_count = display_row_count//2
            extra_row = [["..." for _ in range(col_count + 1)]]
            first_half = data.head(half_count).reset_index().values.tolist()
            second_half = data.tail(half_count).reset_index().values.tolist()
            data = first_half + extra_row + second_half

        if display_col_count < col_count:
            half_count = display_col_count//2
            headers = headers.tolist()
            headers = headers[:half_count] + ['...', ] + headers[-half_count:]
            # convert DataFrame to list if not converted yet,
            if display_row_count >= row_count:
                data = data.reset_index().values.tolist()

            data = [x[:half_count] + ['...'] + x[-half_count:] for x in data]

        return tabulate(data, headers=headers, **options)

    @property
    def _constructor(self):
        # return DataFrameWithHelpers as the datatype in place of DataFrames
        return DataFrameWithHelpers


def plot_confusion_matrix(y_true: Iterable, y_pred: Iterable) -> Axes:
    """
    Plot the confusion matrix given the predictions and true results.
    Parameters
    ----------
    :param array, shape = [n_samples] y_true: Maximum number of rows to print.
    :param array, shape = [n_samples] y_pred: Maximum number of cols to print.
    :return: matplotlib Axes of the confusion matrix plot.
    :rtype: matplotlib Axes
    """
    labels = unique_labels(y_true)
    columns = [f'Predicted {label}' for label in labels]
    index = [f'Actual {label}' for label in labels]
    table = pd.DataFrame(confusion_matrix(y_true, y_pred),
                         columns=columns, index=index)
    return sns.heatmap(table, annot=True, fmt='d', cmap='viridis')


__version__ = '0.0.8'
