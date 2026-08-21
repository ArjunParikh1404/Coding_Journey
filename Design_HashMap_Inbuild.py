# Implement a hash set using inbuild functions.

hashset = set() 

# add a new key
hashset.add(3)
hashset.add(2)
hashset.add(1)
hashset.update([4,5,6]) # For multiple
hashset.update({4,5,6}) # For multiple

print(hashset)

# remove a key
hashset.remove(2) # if we don't have in set then it gives error
hashset.discard(2) # Don't give error
hashset.pop() # Removes first element
# hashset.clear() # Remove everything

# check if the key is in the hash set
if (2 not in hashset):
    print("Key 2 is not in the hash set.")

# get the size of the hash set
print("Size of hashset is:", len(hashset)) 

# iterate the hash set
for x in hashset:
    print(x, end=" ")
print("are in the hash set.")

# clear the hash set
hashset.clear()    
print("Size of hashset:", len(hashset))

# Some Build-in functions
len(hashset)
min(hashset)
max(hashset)
sorted(hashset)
sum(hashset)
list(hashset)
