import pandas as pd

contents = pd.read_csv('Countries.csv')


print(contents)

print(contents['CountryKey'].sum())
