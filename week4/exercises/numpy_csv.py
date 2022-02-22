import numpy as np
from collections import Counter

bef_stats_df = np.genfromtxt(
    "befkbhalderstatkode.csv", delimiter=",", dtype=np.uint, skip_header=1
)
dd = bef_stats_df

german_children_aged_zero = (dd[:, 0] == 2015) & (dd[:, 2] == 0) & (dd[:, 3] == 5180)

def show_population(year, area, age, country_code):
    mask = (
        (dd[:, 0] == year)
        & (dd[:, 2] == age)
        & (dd[:, 3] == country_code)
        & (dd[:, 1] == area)
    )
    return "Population", int(sum(dd[mask][:, 4]))


def show_population_v2(year, area=None, country_code=None, age=None,):
    year_mask = dd[:,0] == year
    area_mask = dd[:,1] if area == None else dd[:,1]==area
    age_mask = dd[:,2] if age == None else dd[:,2]==age
    country_code_mask = dd[:,3] if country_code == None else dd[:,3]==country_code
    mask = (
        (year_mask)
        & (area_mask)
        & (age_mask)
        & (country_code_mask)
    )
    return "Population", int(sum(dd[mask][:, 4]))


def nationals_by_area(year, nationality):
    mask = (dd[:, 0] == year) & (dd[:, 3] == nationality)
    stat_dict = Counter(dd[mask][:, 1])
    biggest_area_by_nationality = max(stat_dict, key=stat_dict.get)
    return biggest_area_by_nationality


def find_area_with_fewest_foreigners(year):
    mask = (dd[:, 0] == year) & (dd[:, 3] != 5100)
    stat_dict = Counter(dd[mask][:, 1])
    area_with_fewest_foreigners = min(stat_dict, key=stat_dict.get)
    return area_with_fewest_foreigners

def find_french_age_by_year(year):
    mask = (dd[:, 0] == year) & (dd[:, 3] == 5130)
    stat_dict = dict(Counter(dd[mask][:, 2]))
    max_value = max(stat_dict.items(), key=lambda x: x[1])
    biggest_age_group = []
    for key, value in stat_dict.items():
        if value == max_value[1]:
            biggest_age_group.append(key)
    return "Age groups with highest amount: ", biggest_age_group
    #return stat_dict


# print("Amount of german children in 2015 aged 0:", int(sum(dd[german_children_aged_zero][:,4])))
# print(show_population(2015,1,18,5100))
print(show_population_v2(2015, 1, 5100))
# print(nationals_by_area(1992, 5244))
# print(find_area_with_fewest_foreigners(1992))
# print(find_area_with_fewest_foreigners(2015))
#print(find_french_age_by_year(2015))