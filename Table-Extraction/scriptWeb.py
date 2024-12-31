import pandas as pd

url = 'https://therahmacenter.org/'

tables = pd.read_html(url)

print(len(tables))
