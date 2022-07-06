import pandas as pd
import csv

df = pd.read_csv('data.csv')

print(df.to_string())