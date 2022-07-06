import pandas as pd

data = {
  "earns": [420, 380, 390],
  "period": [50, 40, 45]
}

x = pd.DataFrame(data)

#x = pd.read_csv('data.csv')


print(x)
print(x.loc[0])
