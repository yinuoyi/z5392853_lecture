"""The purpose of the yf_example3 module is to download stock price data for Qantas for a given year and save the information in a CSV file."""

import os
import toolkit_config as cfg
import yf_example2

toolkit_config = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def qan_prc_to_csv(year):
    """
    Download Qantas stock prices for a given year into a CSV file.
    :param year: an integer representing the year of interest
    """
    startdate = f"{year}-01-01"
    enddate = f"{year}-12-31"
    tic = "QAN.AX"
    filename = f"qan_prc_{year}.csv"
    filepath = os.path.join(toolkit_config, filename)
    yf_example2.yf_prc_to_csv(startdate, enddate, tic, filepath)


if __name__ == "__main__":
    qan_prc_to_csv(2020)
