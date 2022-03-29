import pandas as pd
#"Datasæt: https://www.opendata.dk/city-of-copenhagen/monumenter
#CSV: https://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:monumenter&outputFormat=csv&SRSNAME=EPSG:4326

#1. Hvor mange monumenter er der i København?
url = 'https://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:monumenter&outputFormat=csv&SRSNAME=EPSG:4326'
data = pd.read_csv(url, sep=',')

def monuments_in_cph():
    monument_count = data.shape[0]
    print(monument_count)
    return monument_count

#monuments_in_cph()


#2. Hvor mange monumenter bliver vedligeholdt? Dvs. graffitirenhold = ja
def maintained_monuments():
    m_monuments = data[data['graffitirenhold'].str.contains('Ja') == True]
    num_of_m_monuments = len(m_monuments.index)
    print(num_of_m_monuments)

#maintained_monuments()


#3. Lav en funktion som kan finde koordinaterne på et monument baseret på monumentets id eller navn?
#	F.eks:
#		def monumentById(monumentId):
#			return coordinates

def monuments_coordinates(monument_id):
    data.set_index('id', inplace=True)
    monument = data.loc[monument_id]
    return monument.iloc[6], monument.iloc[7]

#monuments_coordinates(49865)
	
#3.a Vis monument som bliver returneret i metoden, på et kort over københavn ved brug af plotting. (Se afsnittet om 'Folium and Bokeh' under notebooks/03-3 Plotting)
#   Se handin_01_charts

#4. Find navnet på monumentet med x og y koordinaterne eller længde- og breddegraderne?	
#	x = 724407.424966
#	y = 6175719.798486
#	MULTIPOINT ((12.555485308174104 55.69383926601615))

def monument_name_by_coordinates(lon, lat):
    monument = data[(data['longitude'] == lon) & (data['latitude'] == lat)]
    monument_name = monument.iloc[0]['navn']
    print('Navn på monument: ' + monument_name)

#monument_name_by_coordinates(12.587330, 55.670313)

#5. Lav en metode der optegner alle monumenterne på kortet ved brug af plotting.
#   Se handin_01_charts
#6. Gør kortet interaktiv så navnet på monumenterne vises når man trykker på et plot. (Se afsnittet om 'Interactive plots with bokeh' under notebooks/03-3 Plotting)"
#   Se handin_01_charts
