import pandas as pd
df = pd.read_csv('datascience\\5date.csv')
#print(df)
filtered_df = df[['Id', 'Human Development Index HDI-2014']].sort_values(by='Id')
filtered_df.columns = ['Country', 'Value']
desired_countries = [
    'Estonia','Finland', 'Latvia', 'Portugal', 'Lithuania','Sweden'

]
desired_countries_df = filtered_df[filtered_df['Country'].str.strip().isin(map(str.strip, desired_countries))]
desired_countries_df=desired_countries_df.sort_values('Country', ignore_index=True)
print(desired_countries_df)
num_countries = desired_countries_df['Country'].nunique()
print(f'Number of countries indesired_countries_df: {num_countries}')
desired_countries_df.to_csv('humanindex.csv', index=False)
