"""
    This module contains the class to define and work with a
    Data frame object created from a query result
"""

import pandas as pd
import matplotlib.pyplot as plt


class HonoluluDf:
    """A class used to represent an Animal
    Args:
    ----------
    table_result : list
        a tuple list with the db result.
    index_field : str
        field from the db to create the index (can't be the same 'table_vale').
    table_value : str
        field from the db to do the operations (avg, max, min etc..)

    Methods
    -------
    get_df:
        generate a Data frame object.
    get_scatter_plot_data:
        generate a plot type scatter for the given table
    get_hist_plot_data:
        generate a hist plot for the given table
    """
    def __init__(self, table_result, index_field, table_value):
        self.table_result = table_result
        self.table_value = str(table_value)
        self.index_field = index_field

        self.df = pd.DataFrame(self.table_result).sort_values(by=[self.index_field])

    def __str__(self):
        return self.df.__str__()

    def get_df(self):
        return self.df

    def get_scatter_plot_data(self):
        self.df.plot(x=self.index_field, y=self.table_value, kind='scatter')
        plt.show()

    def get_hist_plot_data(self):
        self.df.hist(bins=12)
        plt.show()