from heapq import nlargest
from locale import nl_langinfo
import pandas as pd

def divorced() :
    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=F&Tid=2008K1%2C2020K4&OMR%C3%85DE=000'
    data = pd.read_csv(url, sep=';')

    divorced_2008 = data.iloc[0, 3]
    divorced_2020 = data.iloc[1, 3]

    diff = divorced_2020-divorced_2008
    pct = diff/divorced_2008 * 100

    return pct


def never_married() :
    all_url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&Tid=2020K1%2C2020K2%2C2020K3%2C2020K4&CIVILSTAND=TOT'
    all_data = pd.read_csv(all_url, sep=';', skiprows=range(1,5))
    all_data = all_data[all_data["OMRÅDE"].str.contains("Region") == False]
    population = all_data.groupby('OMRÅDE')['INDHOLD'].sum()
    top_5_cities = population.nlargest(5)

    unmarried_url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&CIVILSTAND=U&Tid=2020K1%2C2020K2%2C2020K3%2C2020K4'
    unmarried_data = pd.read_csv(unmarried_url, sep=';', skiprows=range(1,5))
    unmarried_data = unmarried_data[unmarried_data["OMRÅDE"].str.contains("Region") == False] #Fjerner alle rows hvor der står "Region" som område
    unmarried_population = unmarried_data.groupby('OMRÅDE')['INDHOLD'].sum()
    unmarried_series = unmarried_population[["København", "Aarhus", "Aalborg", "Odense", "Vejle"]]

    combined_series = unmarried_series/top_5_cities * 100

    return combined_series


def marrigal_status_changes():
    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=U%2CG%2CE%2CF&Tid=*&OMR%C3%85DE=101'
    data = pd.read_csv(url, sep=';')
    data['TID'] = data['TID'].map(lambda x: str(x)[:-2])
    data = data[data['TID'].str.contains('2022') == False] #Removes 2022 because we dont't have the full year

    unmarried_data = data[data['CIVILSTAND'].str.contains('Ugift') == True]
    unmarried_yearly = unmarried_data.groupby('TID')['INDHOLD'].sum()

    married_data = data[data['CIVILSTAND'].str.contains('Gift/separeret') == True]
    married_yearly = married_data.groupby('TID')['INDHOLD'].sum()

    widows_data = data[data['CIVILSTAND'].str.contains('Enke') == True]
    widows_yearly = widows_data.groupby('TID')['INDHOLD'].sum()

    divorced_data = data[data['CIVILSTAND'].str.contains('Fraskilt') == True]
    divorced_yearly = divorced_data.groupby('TID')['INDHOLD'].sum()
    
    return unmarried_yearly, married_yearly, widows_yearly, divorced_yearly

def marriage_by_age():
    url ='https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&ALDER=*&CIVILSTAND=U%2CG&Tid=2020K1%2C2020K2%2C2020K3%2C2020K4'
    data = pd.read_csv(url, sep=';')
    data['TID'] = data['TID'].map(lambda x: str(x)[:-2])
    data = data[data['ALDER'].str.contains('I alt') == False]
    data['ALDER'] = data['ALDER'].map(lambda x: str(x)[:-2]).apply(pd.to_numeric)

    unmarried_data = data[data['CIVILSTAND'].str.contains('Ugift') == True]
    unmarried_data = unmarried_data.groupby('ALDER')['INDHOLD'].sum()

    married_data = data[data['CIVILSTAND'].str.contains('Gift/separeret') == True]
    married_data = married_data.groupby('ALDER')['INDHOLD'].sum()

    return unmarried_data, married_data




