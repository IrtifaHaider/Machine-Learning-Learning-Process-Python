# - unordered 
# - unindexed
# - mutable collection 
# - unique elements
# - Uses {} Braces -->	Just like dictionaries (but no key:value)

my_set = {1, 2, 3, 4}

# Duplicates will be removed automatically
my_set2 = {1, 2, 2, 3, 4, 4}
print(my_set2) 

# Empty set (IMPORTANT)
empty_set = set()   # ✅ Correct
not_a_set = {}      # ❌ This is an empty dictionary!
print(empty_set)
print(not_a_set)

#Iterating Over a Set
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)

# Union (A ∪ B)
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)        
print(A.union(B))   # Same result as print(A | B) 

# Intersection (A ∩ B)
print(A & B)             
print(A.intersection(B)) # Same result as print(A & B)

# Difference (A - B)
print(A - B)            
print(A.difference(B))   

# Symmetric Difference (A Δ B) --> Elements in A or B but not both.
print(A ^ B)                    
print(A.symmetric_difference(B))

# Subset / Superset / Disjoint
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))    
print(B.issuperset(A))  
print(A.isdisjoint({3, 4}))  # True → No common items

# Sets Do Not Support Indexing
my_set = {10, 20, 30}
# rint(my_set[0])  # ❌ Error! 'set' object is not subscriptable
print(list(my_set)[0]) # If you need indexing, convert to list


#Sets are Hash-Based --> element lookup is very fast (like dictionaries)
my_set = {10, 20, 30}
print(20 in my_set)    # True
print(40 in my_set)    # False

# Remove duplicates from a list
lst = [1, 2, 2, 3]
unique = set(lst)
print(unique) 

# Checking membership fast
banned_words = {"bad", "hate", "ugly"}
if "bad" in banned_words:
    print("Word not allowed")


# Set Methods
set3 = {1, 2, 3}
set3.add(4)
print("After add(4):", set3)
set3.remove(2)
print("After remove(2):", set3)
set3.discard(10)  # No error if element not present
print("After discard(10):", set3)
set3.pop()
print("After pop():", set3)
set3.clear()
print("After clear():", set3)

# MEMORY USAGE COMPARISON
import sys
my_list2 = [1, 2, 3]
my_set2 = {1, 2, 3}
print("List size:", sys.getsizeof(my_list2))
print("Set size:", sys.getsizeof(my_set2))