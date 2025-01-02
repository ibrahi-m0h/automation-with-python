# This program is meant to extract a list of emails from a Google Sheets csv file and return a random email for a raffle

import pandas as pd
import random 

# Read csv file into dataframe
tables = pd.read_csv('BTG End of the Year Survey 2024-2025 (Responses) - Form Responses 1.csv')

#Extract email column and instantiate into a variable
email_column = tables['Email']

#Convert email_column objects into an array
email_List = list(email_column)

winner = random.choice(email_List)

print(winner)