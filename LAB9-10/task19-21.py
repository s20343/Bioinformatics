import pandas as pd
from scipy import stats

data1 = pd.read_csv('biological_data1.csv')
data2 = pd.read_csv('biological_data2.csv')

values1 = data1['value']
values2 = data2['value']

mean1 = values1.mean()
mean2 = values2.mean()
std1 = values1.std()
std2 = values2.std()

t_statistic, p_value = stats.ttest_ind(values1, values2)


print("Dataset 1 - Mean: {:.2f}, Standard Deviation: {:.2f}".format(mean1, std1))
print("Dataset 2 - Mean: {:.2f}, Standard Deviation: {:.2f}".format(mean2, std2))
print("T-Test - t-statistic: {:.2f}, p-value: {:.4f}".format(t_statistic, p_value))
