import xml.etree.ElementTree as ET
import pandas as pd
from sklearn.linear_model import LinearRegression
xml_data = open('datascience\\UNdata_Export_20231211_231736613.xml', 'r').read()  # Read file
root = ET.XML(xml_data)  # Parse XML

data = []
cols = []

# Find unique field names (column names)
field_names = set()
for record in root.findall(".//record"):
    field_names.update(subchild.get("name") for subchild in record.findall(".//field"))

# Create columns
cols = list(field_names)

# Extract data from records
for record in root.findall(".//record"):
    row_data = {}
    for field in record.findall(".//field"):
        row_data[field.get("name")] = field.text
    data.append(row_data)

# Create DataFrame
df = pd.DataFrame(data, columns=cols)
df['Time Period'] = pd.to_numeric(df['Time Period'], errors='coerce')
# Filter data for the desired columns and years
filtered_df = df[df['Time Period'].between(2013, 2014)][['Reference Area', 'Time Period', 'Observation Value']]
filtered_df.columns = ['Country', 'Year', 'Value']
desired_countries = [
    'Norway', 'Netherlands', 'Germany', 'Canada', 'United States',
    'Australia', 'United Kingdom of Great Britain and Northern Ireland', 'Japan', 'France', 'South Korea',
    'Israel', 'Italy', 'Spain', 'Czech Republic', 'China', 'Brazil',
    'Austria', 'United Arab Emirates', 'Belgium', 'Denmark', 'South Africa',
    'Poland', 'Turkey', 'India', 'Ukraine','United States of America','Republic of Korea','United Kingdom' , 'Estonia','Finland', 'Latvia', 'Portugal', 'Lithuania','Sweden','Switzerlend'
]
# desired_countries_df = filtered_df[filtered_df['Country'].isin(desired_countries)]
# print(desired_countries_df)

# regr=df[df['Reference Area'].isin(['South Africa','India'])][['Reference Area', 'Time Period', 'Observation Value']]
# model = LinearRegression()
# for country in regr['Reference Area'].unique():
#     country_data = regr[regr['Reference Area'] == country]
#     X = country_data['Time Period'].values.reshape(-1, 1)
#     y = country_data['Observation Value'].values
#     model.fit(X, y)
#     predicted_value = model.predict([[2013]])
#     new_row = {'Reference Area': country, 'Time Period': 2013, 'Observation Value': 0}
#     regr=pd.concat([regr, pd.DataFrame(new_row, index=[0])], ignore_index=True)
#     regr.loc[(regr['Reference Area'] == country) & (regr['Time Period'] == 2013), 'Observation Value'] = predicted_value[0]
# regr.columns = ['Country', 'Year', 'Value']
# result= desired_countries_df[(desired_countries_df['Year'] == 2013) | (desired_countries_df['Country'] == 'United Arab Emirates')]
# result['Country'] = result['Country'].str.strip().replace('Republic of Korea', 'South Korea')
# result['Country'] = result['Country'].str.strip().replace('United States of America', 'United States')
# result['Country'] = result['Country'].str.strip().replace('United Kingdom of Great Britain and Northern Ireland', 'United Kingdom')


# result=pd.concat([result, regr.loc[ (regr['Year'] == 2013)]], ignore_index=True).sort_values('Country')
# print(result)
# num_countries = result['Country'].nunique()
# print(f'Number of countries indesired_countries_df: {num_countries}')
# result.to_csv('reserchprocgdp.csv', index=False)

desired_countries2 = [
'Estonia','Finland', 'Latvia', 'Portugal', 'Lithuania','Sweden','Switzerlend'
]
desired_countries_df = filtered_df[filtered_df['Country'].isin(desired_countries2)]
result= desired_countries_df[(desired_countries_df['Year'] == 2013) ]
del result['Year']
result.columns = ['Country', 'Value']
print(result)

df2 = pd.read_csv('C:\Visual\Projects\hello-world\educgdpproc.csv')
df2.columns = ['Country', 'researchgdp']

print(df2)
#2
df0 = pd.read_csv('C:\Visual\Projects\hello-world\commoninformation.csv')
del df0['Population']
del df0['Area (sq. mi.)']

del df0['GDP ($ per capita)']

#3
df3 = pd.read_csv('C:\Visual\Projects\hello-world\electricity.csv')
del df3['Year']
del df3['Value']
del df3['Population']
df3.columns = ['Country', 'Electricity per person']

print(df3)
 #4

#5
df5 = pd.read_csv('C:\Visual\Projects\hello-world\humanindex.csv')
df5.columns = ['Country', 'Human index']

print(df5)
#6
df6 = pd.read_csv('C:\Visual\Projects\hello-world\happyindex.csv')
del df6['Year']

df6.columns = ['Country', 'Happy index']

print(df6)
countriess = ['Estonia','Finland', 'Latvia', 'Lithuania','Portugal', 'Sweden']
result_df = pd.DataFrame({'Country': countriess})
result_df = result_df.sort_values(by='Country').reset_index(drop=True)
datasets = [  df3, df5, df6]
for dataset in datasets:
      if 'Country' in dataset.columns:  # Check if 'Country' column exists in the dataset
        result_df = pd.merge(result_df, dataset, on='Country', how='left')
net_migration=[-3.16, 0.95,-2.23,-0.71,3.57,1.67]
result_df['Net migration'] = [-3.16, 0.95, -2.23, -0.71, 3.57, 1.67]
print(result_df)
result_df.to_csv('forvika.csv', index=False)
