import re

#Create find lists using re from the data/adresses.txt
with open('addresses.txt') as f:
    addresses = f.read()

#Phone numbers
pattern2 = re.compile(r'\d{2} \d{2} \d{2} \d{2}')
phones_numbers = pattern2.findall(addresses)
print('PHONE_NUMBERS:')
print(phones_numbers)

#Zip codes
pattern3 = re.compile(r'\d{4} \d{4} \d{4} \d{4}')
zip_codes = pattern3.findall(addresses)
print('ZIP_CODES:')
print(zip_codes)

#City names with zip code
pattern4 = re.compile(r'\d{4} \w+')
city_zip = pattern4.findall(addresses)
print('CITY_ZIP:')
print(city_zip)

#Street names
pattern5 = re.compile(r'([\w+]+) (\d+\D?)')
street_names = pattern5.findall(addresses)
print('STREET_NAMES:')
print(street_names)

