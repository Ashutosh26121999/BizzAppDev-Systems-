"""
. Provide a program to read the CSV file.
• CSV file has three columns, the first column names, the second column is birthdate(YYYYMM-DD) the third column is salary.
• Read the file and display the data and age in the terminal.
• The file path, delimiter, and quote char are the input by the user.
• The program has to work from the terminal. The input and output have been taken/displayed
on the terminal.
"""
import pandas as pd
from datetime import date

csv_file = input()
dob = input()
delimiter = input()

df = pd.read_csv(csv_file, parse_dates=[dob], sep=delimiter)


# function
def calc_age(bd: pd.Series) -> pd.Series:
    today = pd.to_datetime(date.today())  # convert today to a pandas datetime
    return (today - bd) / pd.Timedelta(days=365.25)  # divide by days to get years


df['age'] = calc_age(df.dob)
print(df)
