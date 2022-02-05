numbers = range(1,21)

oddNumbersList = [n for n in numbers if n%2 != 0]
print(oddNumbersList)


numbers2 = range(2, 10**6+1)
evenNumbersList = [n for n in numbers2 if n%2 == 0]

print(min(evenNumbersList))
print(max(evenNumbersList))
print(sum(evenNumbersList))

numbers3 = range(3, 301)
multiplesOf3 = [n for n in numbers3 if n%3 == 0]
print(multiplesOf3)

numbers4 = range(1,11)
cubes = [n**3 for n in numbers4]
print(cubes)