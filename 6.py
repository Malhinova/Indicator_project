import pandas as pd
df = pd.read_csv('datascience\\6date.csv')
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
filtered_df = df[df['Year'].between(2013, 2016)][['Country', 'Year', 'Index']]
desired_countries = [
 'Estonia','Finland', 'Latvia', 'Portugal', 'Lithuania','Sweden'
]
desired_countries_df = filtered_df[filtered_df['Country'].isin(desired_countries)]
result= desired_countries_df[(desired_countries_df['Year'] == 2016) ]
# result['Country'] = result['Country'].str.strip().replace('Turkiye', 'Turkey')
# result['Country'] = result['Country'].str.strip().replace('Czechia', 'Czech Republic')

result=result.sort_values('Country', ignore_index=True)

print(result)
num_countries = result['Country'].nunique()
print(f'Number of countries indesired_countries_df: {num_countries}')
result.to_csv('happyindex.csv', index=False)
