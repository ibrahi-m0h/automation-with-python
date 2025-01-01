import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1aSIjQNopnSFMrqjldRLPiD0hjF2B8zWjhKDkFwW9m9s/edit?gid=564406339#gid=564406339'

tables = pd.read_html(url)

print(tables[1])
#Output of above is:
# 0   1                 2   3   4
# 0 NaN NaN  Form Responses 1 NaN NaN

# Reason: Google sheets doesn't publish table values in HTML,
# which is why pandas read_html cannot parse through the data
