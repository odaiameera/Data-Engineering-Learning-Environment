print('Hello, World!')

print(5+5)

# Tuples - Immutable sequences, typically used to store collections of heterogeneous data
# Tuples are defined by enclosing the elements in parentheses ()
# Example of a tuple - We can access the elements of a tuple using indexing
# tuple_name[index]
tuple1 = ("disco", 10, 1.2)
tuple1[0]
tuple1[1]
tuple1[2]
# Wew can also use negative indexing to access elements from the end of the tuple
tuple1[-1]
tuple1[-2]
tuple1[-3]
# Tuples are immutable, meaning we cannot change their elements after creation
# However, we can create a new tuple by concatenating existing tuples
tuple2 = ("hard rock", 10)
tuple3 = tuple1+tuple2
tuple3
type(tuple3)
tuple3[0:3]
tuple3[3:5]
# We can also use built-in functions like len() to get the length of a tuple
len(tuple3)
# We can use the count() method to count the occurrences of a specific element in a tuple
tuple3.count(10)
Ratings = (5, 4, 3, 5, 4, 5, 2)
Ratings1 = Ratings
Ratings1
Ratings[2] = 4  # This will raise an error since tuples are immutable
# To modify a tuple, we can convert it to a list, make the changes, and then convert it back to a tuple
# Sorting a tuple returns a list -- I assigned a new variable to the tuple Ratings
Ratings = sorted(Ratings)
# Nestings - Tuples can contain other tuples as elements
nested_tuple = (("rock", 10), ("pop", 8), ("jazz", 9))
# Indexing into nested tuples - We can access elements of nested tuples using multiple indices
nested_tuple[0]
nested_tuple[1]
nested_tuple[2]
nested_tuple[0][0]
nested_tuple[0][1]
nested_tuple[1][0]
nested_tuple[1][1]  # And so on...

# Lists - Mutable sequences, typically used to store collections of homogeneous data
# Lists are defined by enclosing the elements in square brackets []
# Example of a list - We can access the elements of a list using indexing
List = ["disco", 10, 1.2]
# list_name[index]
list1 = ["disco", 10, 1.2]
List[0]
list1[1]
# We can also nest tuples and lists within each other
nested_list = [("rock", 10), ["pop", 8], ("jazz", 9)]
# We can also use a negative indexing to access elements
# We can contactenate lists using the + operator
list2 = ["hard rock", 10]
list3 = list1+list2
list3
type(list3)
List.append("new element")  # Adding an element to the end of the list
List
# Inserting an element at a specific position
List.insert(1, "inserted element")
# Extending the list by adding multiple elements
List.extend(["element1", "element2"])
List.remove(10)  # Removing a specific element from the list
List.pop()  # Removing
list1
del (list1[2])  # Deleting an element at a specific position
listA=[1, 2, 3]
"=A, B, C".split(", ")# Splitting a string into a list
listB=["A", "B", "C"]