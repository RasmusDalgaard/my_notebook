import numpy as np
import pandas as pd

data = np.array([['','Col1','Col2','Col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])

dd = pd.DataFrame(data=data[1:4,1:4], columns=data[0,1:4], index=data[1:4,0])

#print(dd)

col2 = dd['Col2']
#print (col2)

col3 = dd.iloc[:,2]
#print(col3)

element_third = dd.iloc[2,1]
#print(element_third)


#---------------------------------------------------------

data = pd.read_csv('API_EN.ATM.CO2E.KT_DS2_en_csv_v2_1345584.csv', sep=',', skiprows=4)
data_country_index = data.set_index('Country Name')

emission = pd.Series(data_country_index['2014'])

top10_emission = emission.nlargest(10)
print(top10_emission)

