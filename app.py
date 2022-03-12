import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import seaborn as sns

"Ben Clarke"

st.title("CSE 5444")

st.header("Lab 3")

df_data = pd.read_csv("https://raw.githubusercontent.com/CSE5544/data/main/ClimateData.csv")

data = df_data.drop(columns=['Non-OECD Economies'])

st.subheader("Heatmap 1:")

data_1 = data
data_1 = data_1[data_1['Country\year'].apply(lambda x: 'OECD' not in x and 'European Union' not in x)]
data_1 = data_1.set_index('Country\year')
data_1 = data_1.apply(pd.to_numeric, errors='coerce')
data_1 = data_1.dropna()

fig, ax = plt.subplots(figsize=(13, 10))
sns.heatmap(data_1, cmap='inferno', norm=LogNorm())

ax.set_title('Heatmap of Emission for Each Country Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Country')
plt.xticks(rotation=90)
st.write(fig)
st.markdown("Note: Data was collected from the following dataset: https://raw.githubusercontent.com/CSE5544/data/main/ClimateData.csv. Data was removed for any regions that either were more than individual countries, and/or contained missing data. Lastly, heatmap values are scaled logarithmically in order to better see that differences between smaller emission values. ")

st.subheader("Heatmap 2:")

data_2 = data
data_2 = data_2[data_2['Country\year'].apply(lambda x: 'New' not in x)]
data_2 = data_2.set_index('Country\year')
data_2 = data_2.apply(pd.to_numeric, errors='coerce')
data_2 = data_2.fillna(100000) 

fig, ax = plt.subplots(figsize=(6, 9))
sns.heatmap(data_2, cmap='rainbow', vmin=10000, vmax=100000)

ax.set_title('Climate Change is Hurting the World')
ax.set_xlabel('Year')
ax.set_ylabel('Country')
plt.xticks(rotation=90)
st.write(fig)

st.subheader("New Visualization:")

data_3 = data.melt(id_vars=["Country\year"], 
        var_name="Year", 
        value_name="Emission")
data_3 = data_3.dropna()
data_3 = data_3[data_3['Country\year'].apply(lambda x: 'OECD' not in x and 'European Union' not in x)]
data_3['Emission'] = data_3['Emission'].apply(pd.to_numeric, errors='coerce')
fig, ax = plt.subplots(figsize=(10,10))
sns.scatterplot(data=data_3, x="Year", y="Emission",
                hue="Country\year")
sns.lineplot(data=data_3, x="Year", y="Emission",
                hue="Country\year")
ax.set_yscale('log')
ax.set_title('Scatterplot of Emission for Each Country Over Time')
plt.xticks(rotation=90)
plt.legend(bbox_to_anchor=(1.01, 1),
           borderaxespad=0)
st.write(fig)