
#Tehtävä 1
furniture = ['table', 'chair', 'shelf', 'sofa', 'bed']

print(furniture)

print(furniture[:2])

print("First two items using a loop:")
for i in range(2):
    print(furniture[i])

if 'sofa' in furniture:
    print("Sofa is in the list")
else:
    print("Sofa is not in the list")
    
    
#Tehtävä 2

thrownDiceNumbers = []
import random
for _ in range(5):
    thrownDiceNumbers.append(random.randint(1, 6)) 

print(thrownDiceNumbers)

sum_of_numbers = sum(thrownDiceNumbers)
print(sum_of_numbers)

highest_value = max(thrownDiceNumbers)
print("Highest value of the dice numbers:", highest_value)

#Tehtävä 3

numbers = []


while len(numbers) < 5:
    num = random.randint(1, 20)
    if num not in numbers:
        numbers.append(num)

print("Random numbers picked:", numbers)
