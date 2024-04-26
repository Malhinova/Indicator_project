import pandas as pd
df = pd.read_csv('datascience\\karina.csv')
print(df)
#df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
filtered_df = df[['Country Name','2015 [YR2015]']].copy()
filtered_df.columns = ['Country', 'Value']
desired_countries = [
'Estonia','Finland', 'Latvia', 'Portugal', 'Lithuania','Sweden'
]
desired_countries_df = filtered_df[filtered_df['Country'].isin(desired_countries)]
# desired_countries_df.loc[desired_countries_df['Country'] == 'United Arab Emirates', 'Value'] = 3.9
# desired_countries_df['Country'] = desired_countries_df['Country'].str.strip().replace('Korea, Rep.', 'South Korea')
# desired_countries_df['Country'] = desired_countries_df['Country'].str.strip().replace('Turkiye', 'Turkey')
# desired_countries_df['Country'] = desired_countries_df['Country'].str.strip().replace('Czechia', 'Czech Republic')
desired_countries_df=desired_countries_df.sort_values('Country', ignore_index=True)
print(desired_countries_df)
num_countries = desired_countries_df['Country'].nunique()
print(f'Number of countries in desired_countries_df: {num_countries}')
desired_countries_df.to_csv('educgdpproc.csv', index=False)
