import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
employee_data = pd.read_csv('Employee.csv', delimiter = ',')
performance_data = pd.read_csv('PerformanceRating.csv', delimiter = ',')
# We gebruiken een 'inner join' omdat we alleen werknemers willen die in beide datasets voorkomen.
combined_data = pd.merge(employee_data, performance_data, on='EmployeeID', how='inner')

# Stap 3: Inspecteer het gecombineerde resultaat
print(combined_data.head())  # Laat de eerste paar rijen van de gecombineerde dataset zien
# Verdeling van werknemers per department
department_count = combined_data['Department'].value_counts()
st.title('Werknemers Verdeling per Department')
st.bar_chart(department_count)
# Maak een histogram met Matplotlib
st.header('Leeftijdsverdeling van Werknemers')

fig, ax = plt.subplots()
ax.hist(combined_data['Age'], bins=10, color='skyblue', edgecolor='black')
ax.set_xlabel('Leeftijd')
ax.set_ylabel('Aantal werknemers')
ax.set_title('Leeftijdsverdeling')

# Toon de Matplotlib grafiek in Streamlit
st.pyplot(fig)
gender_count = combined_data['Gender'].value_counts()
fig, ax = plt.subplots()
ax.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%')
st.pyplot(fig)
st.header('Job Satisfaction versus Years at Company')
fig, ax = plt.subplots()
sns.scatterplot(data=combined_data, x='YearsAtCompany', y='JobSatisfaction', ax=ax)
st.pyplot(fig)
st.header('Attrition versus Salaris')
attrition_filter = st.selectbox('Toon alleen medewerkers die vertrokken of bleven', ['Alle', 'Ja', 'Nee'])

if attrition_filter != 'Alle':
    df = combined_data[combined_data['Attrition'] == attrition_filter]

fig, ax = plt.subplots()
sns.boxplot(data=combined_data, x='Attrition', y='Salary', ax=ax)
st.pyplot(fig)
st.header('Training per JobRole')
training_filter = st.slider('Kies het aantal trainingen:', min_value=0, max_value=combined_data['TrainingOpportunitiesTaken'].max())
df_filtered = combined_data[combined_data['TrainingOpportunitiesTaken'] >= training_filter]

fig, ax = plt.subplots()
sns.barplot(data=df_filtered, x='JobRole', y='TrainingOpportunitiesTaken', ax=ax)
st.pyplot(fig)

