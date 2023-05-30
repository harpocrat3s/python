# This is another simple Python exercise I completed while learning the language
# on the great https://codechalleng.es platform, where I worked on many 
# "PyBites" challenges.

# Assignment:
# For this Bite we got some fake Excel sales data which we are going to analyze 
# with pandas.


import os
from urllib.request import urlretrieve

import pandas as pd

TMP = os.getenv("TMP", "/tmp")
EXCEL = os.path.join(TMP, 'order_data.xlsx')
if not os.path.isfile(EXCEL):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/order_data.xlsx',
        EXCEL
    )


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    # Load the specified sheet from the excel file into a DataFrame
    sales_orders = pd.read_excel(excel, sheet_name='SalesOrders')
    return sales_orders


def get_year_region_breakdown(df):
    # Group the DataFrame by year and region, summing the Total
    # column. You probably need to make an extra column for
    # year, return the new df as shown in the Bite description

    data_frame = df[['OrderDate', 'Region', 'Total']]
    # Convert the OrderDate column to datetime format and extract the year
    data_frame['Years'] = pd.to_datetime(df['OrderDate']).dt.year
    # Group the data frame by Years and Region, summing the Total column
    yearly_sales = data_frame.groupby(['Years', 'Region'])['Total'].sum()
    # Rename the index columns
    yearly_sales = yearly_sales.rename_axis(['Year', 'Region'])
    return yearly_sales.squeeze()


def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    data_frame = df[['Rep', 'Total']]
    # Group the data frame by the Rep column, summing the Total column
    rep_sales = data_frame.groupby([data_frame['Rep']])['Total'].sum()
    # Find the sales rep with the maximum sales
    best_sales_rep = rep_sales.idxmax()
    # Get the total sales for the best sales rep
    total_sales = rep_sales[best_sales_rep]
    return (best_sales_rep, total_sales)


def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    data_frame = df[['Item', 'Units']]
    # Group the data frame by the Item column, summing the Units column
    item_sales = data_frame.groupby([data_frame['Item']])['Units'].sum()
    # Find the item with the maximum units sold
    most_sold_item = item_sales.idxmax()
    # Get the total units sold for the most sold item
    total_units = item_sales[most_sold_item]
    return (most_sold_item, total_units)

print(get_year_region_breakdown(load_excel_into_dataframe(EXCEL)))