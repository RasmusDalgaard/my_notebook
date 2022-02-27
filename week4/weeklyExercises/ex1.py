import numpy as np

bef_stats_df = np.genfromtxt(
    "befkbhalderstatkode.csv", delimiter=",", dtype=np.uint, skip_header=1
)
dd = bef_stats_df

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

def people_by_area():
    year_mask = dd[:,0] == 2015  
    set_of_areas = np.unique(dd[:,1])    
    freq_areas = np.array([np.sum(dd[year_mask & (dd[:,1] == area)][:,4]) 
                      for area in set_of_areas])
    dict_from_arr = dict(zip(set_of_areas, freq_areas))
        
    return dict_from_arr


def people_over_65():
    year_mask = dd[:,0] == 2015
    age_mask = dd[:,2] > 65
    mask = year_mask & age_mask

    return int(sum(dd[mask][:,4]))

def vesterbro():
    year_range = range(1992, 2016)
    area_mask = dd[:, 1] == 4
    pop_year = np.array(
        [np.sum(dd[area_mask & (dd[:, 0] == year)][:, 4]) for year in year_range]
    )
    dict_from_arr = dict(zip(year_range, pop_year))
    return dict_from_arr


def østerbro():
    year_range = range(1992, 2016)
    area_mask = dd[:, 1] == 2
    pop_year = np.array(
        [np.sum(dd[area_mask & (dd[:, 0] == year)][:, 4]) for year in year_range]
    )
    dict_from_arr = dict(zip(year_range, pop_year))
    return dict_from_arr


