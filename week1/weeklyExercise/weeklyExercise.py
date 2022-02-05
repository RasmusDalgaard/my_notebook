#1. Create 5 list comprehensions to solve the following 5 problems:

from argparse import REMAINDER
import math 
import re

#A. Iterate a list of names to return a list of the names starting with H
names = ["Hans", "Mathilde", "Otto", "Hilda"]
namesWithH = [n for n in names if n[0] == "H"]
print(namesWithH)
print()

#B. In one line create a list of the numbers 1-100 to the power of 3
cubes = [n**3 for n in range(1,101)]
print(cubes)
print()

#C. Iterate a list of names to create a list of tuples where the tuples first value is the length of the name and the second is the name
nameTuples = [tuple([len(n), n]) for n in names]
print(nameTuples)
print()

#D. Iterate over each character in a string and get only those that are nummeric
myString = "I am 23 and my IQ is 25 plus 5"
numbersInString = [int(n) for n in myString.split() if n.isdigit()]
print(numbersInString)
#Alternative solution using RegEx
numbersInString2 = [int(n) for n in re.findall(r'\b\d+\b', myString)]
print("Alternative solution: ")
print(numbersInString2)
print()

#E. Using only a list comprehension wrapped in set() get all possible combinations from throwing 2 dice (hint use 2 for loops in a single list comprehension). 
#Result should look like: [2,3,4,5,6,7,8,...] or a more complex/accurate solution: [(1,1),(1,2)...] in a way that (1,2) is equal to (2,1).
combos = [(d1, d2) for d1 in range(1,7) for d2 in range(1,7)]
print(combos)
print()

#######################################

#2. Create 2 dictionary comprehensions to solve the following:

#A. Iterate a list of names and create a dictionary where key is the name and value is the length of the name
listOfNames = ["Rasmus", "Gitte", "Bent", "Manfred"]
myDict = {key:len(key) for key in listOfNames}
print(myDict)
print()

#B. Iterate a list of numbers and create a dictionary with {key:value} being {number:squareroot_of_number}
listOfNumbers = [4, 9, 25, 36, 81]
sqrtDict = {key:math.sqrt(key) for key in listOfNumbers}
print(sqrtDict)
print()



#3. Extra assignment (This one goes beyond what is covered in the course notebooks. So only do it if you want an extra challenge).
#A. Progammatically using loops create a small program to produce a dictionary with all the 2 dice throw combinations as keys (eg: 2,3,4...etc) 
#and their likelyhood in percent as values
def propabilityFunc(d1, d2):
    propability = 0
    diceRes = d1 + d2
    if diceRes <= 7:
        propability = (diceRes-1)/36*100
    elif diceRes >= 8:
        propability = (13%diceRes)/36*100
    return propability

diceDict = {(d1 + d2): propabilityFunc(d1,d2) for d1 in range(1,7) for d2 in range(1,7)}
print(diceDict)