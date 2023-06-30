import pandas as pd

data = pd.read_excel('sequence_data.xlsx')


statistics = data[['Property1', 'Property2']].describe()


print(statistics)
