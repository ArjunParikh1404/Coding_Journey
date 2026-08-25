# Implement a hashMap using inbuild functions.

# Creating a HashMap
d = {0:5, 3:6, 2:7}

# insert a new (key, value) pair or update the value of existed key
d[1] = 8 
d[2] = 9
d["no"] = 5

print(d)

# get the value of a key
print(d[3]) # Can give error
print(d.get(100)) # Can't give error

# delete a key
del d[3]
del d["no"]

print(d)

# check if a key is in the hash map
if 3 not in d:
    print("Key 3 is not in the hash map.")
    
print(len(d))

# iterate the hash map
for key in d:
    print("(" + str(key) + "," + str(d[key]) + ")", end=" ")
    
# get all keys in hash map
print(d.keys())

print(d.values())

# pop()
x = d.pop(2)
print(x)
print(d)

# items()
for key, value in d.items():
    print(key, value)

# clear(), update(), copy(), popitem()
