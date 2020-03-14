import numpy as np 
import pandas as pd 

#Data sets to clean:
#	1. GINI Index (World Bank)
#	2. Internally Displaced Persons (World Bank)
#	3. Total Population (World Bank)
#	4. Gender Parity Index - School Enrollment (World Bank)


#	US Foreign Aid Spending (USAID)


#	Target Data:
#	Governance Indicators

#Function to clean & pickle first 4 datasets
def WorldBankData(filename, varname):
    years = [str(year) for year in range(2002, 2019)]
    df = pd.read_csv(filename, skiprows=[0,2])
    return df[['Country Name','Country Code'] + years].to_pickle(
    	'./interim/' + varname + '.pkl')

WorldBankData('./raw/GINI.csv', 'gini')
WorldBankData('./raw/InternallyDisplacedPersons.csv', 'displaced')
WorldBankData('./raw/Population.csv', 'population')
WorldBankData('./raw/SchoolEnrollment_GenderParityIndex.csv', 'gpi_school')