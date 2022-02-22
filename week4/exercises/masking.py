import numpy as np

data = np.arange(1,101).reshape(10,10)

even_numbers = data[data%2 == 0]

string_data = [[str(element) for element in index]for index in data]
print(string_data)

print(even_numbers)