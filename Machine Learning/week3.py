import pandas as pd
import numpy as np
file = pd.ExcelFile('Energy Indicators.xls')
print (file)
file.sheet_names

energy = file.parse('Energy')
energy = energy[16:243]
#print (energy)

energy = energy.drop(['Unnamed: 0', 'Unnamed: 1'],axis=1)

energy = energy.rename(index=str, columns={"Environmental Indicators: Energy": "Country", "Unnamed: 3": "Energy Supply",
                                          "Unnamed: 4": "Energy Supply per Capita","Unnamed: 5": "% Renewable"})
energy.replace('...', np.nan,inplace = True)
energy['Country'] = energy['Country'].str.replace('\d+', '')
energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
energy['Country'] = energy['Country'].replace({"Republic of Korea": "South Korea",
"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong"})
#print (energy['Energy Supply'])
energy['Energy Supply'] = energy['Energy Supply'].apply(pd.to_numeric, errors='coerce')
print (type(energy['Energy Supply']))
energy['Energy Supply'] = energy['Energy Supply']*1000000
#print (energy['Energy Supply'])


#GDP = pd.read_csv('world_bank.csv',skiprows=3,  names=['Country Name','Country Code'])
col = pd.read_csv('world_bank.csv',skiprows=4, nrows=1).columns
GDP = pd.read_csv('world_bank.csv',skiprows=4,  names=col)
GDP.rename(columns={'Country Name': 'Country'}, inplace=True)
GDP['Country'] = GDP['Country'].replace({"Korea, Rep.": "South Korea", 
"Iran, Islamic Rep.": "Iran",
"Hong Kong SAR, China": "Hong Kong"})
GDP = GDP.drop(['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
       '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
       '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
       '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
       '2005'],axis=1)

file1 = pd.ExcelFile('scimagojr-3.xlsx',index_col=0, skiprows=1)
file1.sheet_names
ScimEn = file1.parse('Sheet1')
df = pd.merge(pd.merge(energy, GDP, on='Country'), ScimEn, on='Country')

#df2.index_col=['Country']
df.set_index('Country',inplace=True)
df = df[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
df = (df.loc[df['Rank'].isin([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])])
df.sort('Rank',inplace=True)
print (df)

def answer_one():
    return df