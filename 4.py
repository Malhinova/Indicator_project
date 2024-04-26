import pandas as pd
df = pd.read_csv('datascience\\4date.csv')
filtered_df = df[['Country', 'Population', 'Area (sq. mi.)', 'Net migration', 'GDP ($ per capita)']]
filtered_df.to_string()
desired_countries = [
    'Estonia','Finland', 'Latvia', 'Portugal', 'Lithuania','Sweden'

]
desired_countries_df = filtered_df[filtered_df['Country'].str.strip().isin(map(str.strip, desired_countries))]
#desired_countries_df['Country'] = desired_countries_df['Country'].str.strip().replace('Korea, South', 'South Korea')
desired_countries_df=desired_countries_df.sort_values('Country', ignore_index=True)
print(desired_countries_df)
num_countries = desired_countries_df['Country'].nunique()
#print(f'Number of countries indesired_countries_df: {num_countries}')
desired_countries_df.to_csv('commoninformation.csv', index=False)
