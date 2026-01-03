"""
IBM Data Science - Python Fundamentals: Tuples and Lists
This script demonstrates the differences between immutable Tuples 
and mutable Lists, following PEP 8 formatting guidelines.
"""

# =============================================================================
# 1. TUPLES (Immutable - Cannot be changed)
# =============================================================================

# Initialization with heterogeneous data
tuple1 = ("disco", 10, 1.2)

# Accessing elements via indexing
# tuple_name[index]
first_element = tuple1[0]
last_element = tuple1[-1]  # Negative indexing

# Concatenating tuples (creates a NEW tuple)
tuple2 = ("hard rock", 10)
tuple3 = tuple1 + tuple2

# Slicing: tuple[start:stop] -> (stop index is excluded)
# This gets elements at index 0, 1, and 2
slice_sample = tuple3[0:3]

# Built-in functions for tuples
length_of_tuple = len(tuple3)
count_of_ten = tuple3.count(10)

# Immutability Check:
# The following line would raise a TypeError:
# tuple1[0] = "pop" 

# Sorting a tuple returns a LIST
ratings = (5, 4, 3, 5, 4, 5, 2)
sorted_ratings = sorted(ratings)

# Nesting: Accessing nested data using multiple indices
nested_tuple = (("rock", 10), ("pop", 8), ("jazz", 9))
genre_score = nested_tuple[0][1]  # Returns 10


# =============================================================================
# 2. LISTS (Mutable - Can be changed)
# =============================================================================

# Initialization
list1 = ["disco", 10, 1.2]
list2 = ["hard rock", 10]

# Concatenation
list3 = list1 + list2

# --- Modifying Lists (Mutating) ---

# Adding elements
list1.append("new element")        # Adds to the very end
list1.insert(1, "inserted item")   # Adds "inserted item" at index 1

# Extending (adds multiple elements as individual items)
list1.extend(["element1", "element2"])

# Removing elements
list1.remove("disco")              # Removes specific value
popped_item = list1.pop()          # Removes and returns the last item
del list1[0]                       # Deletes item at specific index


# =============================================================================
# 3. HELPFUL CONVERSIONS
# =============================================================================

# Splitting a string into a list based on a delimiter
string_data = "A, B, C"
split_list = string_data.split(", ")

# Converting between types
tuple_version = tuple(list1)
list_version = list(tuple_version)

if __name__ == "__main__":
    # Demonstration of output
    print(f"Original Tuple: {tuple1}")
    print(f"Sorted Ratings (List): {sorted_ratings}")
    print(f"Modified List: {list1}")
    print(f"Split String: {split_list}")