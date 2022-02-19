with open("lexiko.txt", 'r+') as f:
   f = f.read()

print(f)

first = { "x":3,"y":4,"name":"bob" }
second = { "x":13,"y":-4,"name":"malory" }
third = { "x":-3,"y":104,"name":"trudy" }
fourth = { "x":1,"y":14,"name":"alice" }
lexiko = { "First" : first , "Second" : second ,"Third" : third , "Fourth" : fourth }

print("")
print("Key Words :  ")
print(first.keys())
print("")
print("Pick A Key :  ")

a = input()

if a in first.keys() :
    val1 = first[a]

if a in second.keys() :
    val2 = second[a]

if a in fourth.keys() :
    val3 = third[a]

if a in fourth.keys() :
    val4 = fourth[a]



if val1 > val2 and val1 > val3 and val1 > val4 :
    maxval = val1

if val2 > val1 and val2 > val3 and val2 > val4 :
    maxval = val2

if val3 > val1 and val3 > val2 and val3 > val4 :
    maxval = val3

if val4 > val1 and val4 > val2 and val4 > val3:
    maxval = val4



if val1 < val2 and val1 < val3 and val1 < val4:
    minval = val1

if val2 < val1 and val2 < val3 and val2 < val4:
    minval = val2

if val3 < val1 and val3 < val2 and val3 < val4:
    minval = val3

if val4 < val1 and val4 < val2 and val4 < val3:
    minval = val4

print("Min Value : ")
print(minval)
print("Max Value : ")
print(maxval)