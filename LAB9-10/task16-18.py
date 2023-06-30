import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('vaccination_data.csv')

age_groups = data['Age group']
vaccinated = data['Number vaccinated']

plt.bar(age_groups, vaccinated)

plt.xlabel('Age group')
plt.ylabel('Number vaccinated')
plt.title('COVID-19 Vaccination by Age Group')

# Display the chart
plt.show()
