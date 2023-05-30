# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.
# This was the assignment: In this Bite you are asked to complete a number of 
# functions that each create a pandas Series. How you create each series is up to you.

import string
import pandas as pd
import numpy as np


def basic_series() -> pd.Series:
    """Create a pandas Series containing the values 1, 2, 3, 4, 5
    Don't worry about the indexes for now.
    The name of the series should be 'Fred'
    """
    # Create a Series with values 1, 2, 3, 4, 5 and name it 'Fred'
    s = pd.Series([x for x in range(1, 6)], dtype=np.int64, name='Fred')
    return s


def float_series() -> pd.Series:
    """Create a pandas Series containing all the values
    from 0.000 -> 1.000 e.g. 0.000, 0.001, 0.002... 0.999, 1.000
    Don't worry about the indexes or the series name.
    """
    # Create a Series with values ranging from 0.000 to 1.000 in steps of 0.001
    s = pd.Series([x for x in np.arange(0.000, 1.001, 0.001)], dtype=np.float64)
    return s


def alpha_index_series() -> pd.Series:
    """Create a Series with values 1, 2, ... 25, 26 of type int64
    and add an index with values a, b, ... y, z
    so index 'a'=1, 'b'=2 ... 'y'=25, 'z'=26
    Don't worry about the series name.
    """
    # Create a list of alphabets from 'a' to 'z'
    alphabet = list(string.ascii_lowercase)
    # Create a Series with values 1 to 26 and use the alphabet list as the index
    s = pd.Series([x for x in range(1, 27)], index=alphabet)
    return s


def object_values_series() -> pd.Series:
    """Create a Series with values A, B, ... Y, Z of type object
    and add an index with values 101, 102, ... 125, 126
    so index 101='A', 102='B' ... 125='Y', 126='Z'
    Don't worry about the series name.
    """
    # Create a list of uppercase alphabets from 'A' to 'Z'
    alphabet = list(string.ascii_uppercase)
    # Create a Series with alphabet values and use a range of numbers as the index
    s = pd.Series(alphabet, index=[x for x in range(101, 127)])
    return s
