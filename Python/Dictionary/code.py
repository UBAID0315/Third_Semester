Mathematics_Students = 45
Science_Students = 35
Math_Science_Students = 20

set_Math = {Mathematics_Students}
set_Science = {Science_Students}
set_both = {Math_Science_Students}

print("Union of Students: ", set_Math | set_Science)
print("Union of Students: ", set_Math.union(set_Science),"\n")
print("Intersaction of Students: ", set_Math & set_Science)
print("Intersaction of Students: ", set_Math.intersection(set_Science),"\n")
print("Mathematics Student: ", Mathematics_Students - Math_Science_Students)
print("Science Students: ", Science_Students - Math_Science_Students)
----------------------------------------------------------------------------------------------
input = "Hello world! This is simple world"
my_dict = {}
frequency = 0

words = input.split()
my_dict["input"] = words

for word in words:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

for i,frequency in my_dict.items():
    print(f'{i}: {frequency}')
  ----------------------------------------------------------------------------------
my_dict = {'rope': 1,'torch': 6, 'gold coins': 42,"dagger": 1,'arrow': 12}

print("Player Inventory: \n")

for keys,values in my_dict.items():
    print(f'{keys} : {values}')

print("Total number of items: ",sum(my_dict.values()))
