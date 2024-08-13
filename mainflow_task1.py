####################
####### LIST #######
####################

# creating a list
arr = []

# adding elements into list
n = int(input("Enter the size of the list : "))
print("Enter elements : ")
for i in range(n):
    arr.append(int(input()))

# printing elements of list
print("\nList : ")
n = len(arr)
for i in range(n):
    print(arr[i], end=" ")

# removing the element
rem = int(input("\n\nEnter the value from the List to remove : "))
arr.remove(rem)

# list after removing last element
print("\nList after removing the value : ", rem)
n = len(arr)
for i in range(n):
    print(arr[i], end=" ")

# Modifying the element of the list
ind = int(input("\n\nEnter the index of element to modify : "))
el = int(input("\nEnter the value : "))
arr.insert(ind, el)

# list after modifying the list
print("\nList after modifying the value : ")
n = len(arr)
for i in range(n):
    print(arr[i], end=" ")

####################
#### DICTIONARY ####
####################
Numbers = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

print("Dictionary information :- \n")
# displaying keys
print(Numbers.keys())

# displaying values
print(Numbers.values())

# displaying items
print(Numbers.items())

# adding items in the dictionary
print("\nADDITION ")
key = int(input("Enter key to insert : "))
value = input("Enter value to insert : ")
Numbers[key] = value

# dictionary after the item is added
print("Dictionary after addition : ", end=" ")
print(Numbers.items())

# deleting the item with the key
print("\nDELETION ", end=" ")
rem = int((input("\nEnter the key of the item to delete : ")))
del Numbers[rem]

# dictionary after the item is deleted
print("Dictionary after removing the item : ", end=" ")
print(Numbers.items())

# Modifying existing values
print("\nMODIFICATION")
key = int(input("Enter the key of the item for modification : "))
value = input("Enter the value of the item for modification : ")
Numbers[key]=value

# dictionary after the item is modified
print("Dictionary after modifying the item : ", end=" ")
print(Numbers.items())

####################
####### SET ########
####################
# Initialize an empty set
my_set = set()
print("Initial set:", my_set)

# Add an element
n = int(input("Enter the size of the set : "))
print("Enter elements : ")
for i in range(n):
    element_to_add = input().strip()
    my_set.add(element_to_add)
print("\nAfter adding the element:", my_set)

# Remove an element
element_to_remove = input("Enter the element to remove: ").strip()
if element_to_remove in my_set:
    my_set.remove(element_to_remove)
    print("\nAfter removing the element:", my_set)
else:
    print(f"Element '{element_to_remove}' not found in the set.")

# Modify an element
old_element = input("Enter the element to modify: ").strip()
if old_element in my_set:
    my_set.remove(old_element)
    new_element = input("Enter the new element: ").strip()
    my_set.add(new_element)
    print("\nAfter modifying the element:", my_set)
else:
    print(f"Element '{old_element}' not found in the set.")

# Display the set
print("Final set:", my_set)
