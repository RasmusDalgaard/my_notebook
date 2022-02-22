import numpy as np

data = np.arange(1,101).reshape(10,10)

even_numbers = data[data%2 == 0]
print(even_numbers)

end_with_6 = np.where(data%10 == 6)
print(data[end_with_6])
