import pandas as pd
df = pd.read_csv('datascience\\karina.csv')
print(df)
#df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
filtered_df = df[df['Year'].between(2013, 2016)][['Country', 'Sector of employment','Year','Value','Gender', 'Field of R&D', 'FUNCTION']]
total = filtered_df[(filtered_df['Sector of employment'] == 'Total intramural') & (filtered_df['Gender'] == 'Total') & (filtered_df['Field of R&D'] == 'Total')
                     &(filtered_df['FUNCTION'] == 'RSE') ]
desired_countries = [
    'Norway', 'Netherlands', 'Germany', 'Canada', 'United States',
    'Australia', 'United Kingdom of Great Britain and Northern Ireland', 'Japan', 'France', 'South Korea',
    'Israel', 'Italy', 'Spain', 'Czech Republic', 'China', 'Brazil',
    'Austria', 'United Arab Emirates', 'Belgium', 'Denmark', 'South Africa',
    'Poland', 'Turkey', 'Turkiye' ,'India', 'Ukraine','United States of America','Republic of Korea','United Kingdom', 'Czechia', 'France incl. Monaco', 'Italy and San Marino','Norway including Svalbard and Jan Mayen Islands'
]
austrmean=df[(df['Country']=='Australia') & (df['FUNCTION']== 'RSE') & ((df['Year']==2013) | (df['Year']==2012) | (df['Year']==2014) )][['Country', 'Sector of employment','Year','Value','Gender', 'Field of R&D', 'FUNCTION']]
braz=df[df['Country']=='Brazil'][['Country', 'Sector of employment','Year','Value','Gender', 'Field of R&D', 'FUNCTION']]
#print(braz)
desired_countries_df =total[total['Country'].isin(desired_countries)]
result= desired_countries_df[(desired_countries_df['Year'] == 2013) ]
#print(result)
num_countries = df['Country'].nunique()
print(f'Number of countries indesired_countries_df: {num_countries}')
