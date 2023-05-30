#!/usr/bin/env python3

# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.

# The assignment: In [the previous bite] we looked at creating some simple pandas 
# Series. In this Bite we continue where we left off and look at retrieving values 
# and indexes of different types from Series.

import numpy as np
import pandas as pd


def return_at_index(ser: pd.Series, idx: int) -> object:
    """Return the Object at the given index of the Series
    If you want to be extra careful catch and raise an error if
       the index does not exist.
    """
    try:
        return ser[idx]
    except KeyError as e:
        raise KeyError(f"Index '{idx}' does not exist in the Series.") from e


def get_slice(ser: pd.Series, start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end.
    """
    return ser.loc[start:end-1]


def get_slice_inclusive(ser: pd.Series,
                        start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end inclusive.
    """
    return ser.loc[start:end]


def return_head(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the first num elements of the given Series.
    """
    return ser.head(num)


def return_tail(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the last num elements of the given Series.
    """
    return ser.tail(num)


def get_index(ser: pd.Series) -> pd.core.indexes.base.Index:
    """Return all indexes of the given Series.
    """
    return ser.index


def get_values(ser: pd.Series) -> np.ndarray:
    """Return all the values of the given Series.
    """
    return ser.values


def get_every_second_indexes(ser: pd.Series,
                             even_index=True) -> pd.core.series.Series:
    """Return all rows where the index is either even or odd.
    If even_index is True return every index where idx % 2 == 0
    If even_index is False return every index where idx % 2 != 0
    Assume default indexing i.e. 0 -> n
    """
    if even_index:
        return ser.loc[[x for x in ser.index if x % 2 == 0]]
    else:
        return ser.loc[[x for x in ser.index if x % 2 != 0]]


def float_series():
    """Returns a pandas Series containing floats"""
    return pd.Series([float(n) / 1000 for n in range(0, 1001)])
