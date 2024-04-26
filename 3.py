import xml.etree.ElementTree as ET
import pandas as pd
xml_data = open('datascience\\3date.xml', 'r').read()  # Read file
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
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
filtered_df = df[df['Year'].between(2013, 2016)][['Country or Area', 'Year', 'Value']]
filtered_df.columns = ['Country', 'Year', 'Value']
desired_countries = [
    'Estonia','Finland', 'Latvia', 'Portugal', 'Lithuania','Sweden'
]
desired_countries_df = filtered_df[filtered_df['Country'].isin(desired_countries)]

result= desired_countries_df[(desired_countries_df['Year'] == 2016) ]
result=result.sort_values('Country')
df2 = pd.read_csv('C:\Visual\Projects\hello-world\commoninformation.csv')
df2.columns = ['Country', 'Population', 'Area (sq. mi.)', 'Net migration', 'GDP ($ per capita)']
population=df2['Population'].to_list()
result['Population']=population
result['Population']= pd.to_numeric(result['Population'], errors='coerce')
result['Value']= pd.to_numeric(result['Value'], errors='coerce')
result['Value/Population']=result['Value']/result['Population']
# result['Country'] = result['Country'].str.strip().replace('Republic of Korea', 'South Korea')
# result['Country'] = result['Country'].str.strip().replace('United States of America', 'United States')
# result['Country'] = result['Country'].str.strip().replace('France incl. Monaco', 'France')
# result['Country'] = result['Country'].str.strip().replace('Italy and San Marino', 'Italy')
# result['Country'] = result['Country'].str.strip().replace('Norway including Svalbard and Jan Mayen Islands', 'Norway')
# result['Country'] = result['Country'].str.strip().replace('Czechia', 'Czech Republic')

result=result.sort_values('Country', ignore_index=True)

print(result)
num_countries = result['Country'].nunique()
print(f'Number of countries indesired_countries_df: {num_countries}')
result.to_csv('electricity.csv', index=False)
