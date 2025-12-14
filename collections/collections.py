# list - indexed, ordered, allow duplicates, mutable

fruits = [ "oranges", "apples", "apples", "blueberries", "bananas", "bananas", "strawberries" ]

# set - not indexed, unordered, no duplicates, mutable
employee_emails = {"alice@corporation.com", "bob@corporation.com", "devantre@corporation.com"}

# tuple - indexed, ordered, allow duplicates, immutable
coordinate = (40.7128, -74.0060)

# dictionary - not indexed, unordered, keys must be unique, mutable
employee_info = {"name": "Alice", "age": 30, "email": "alice@corporation.com"}

# ------------
# list comprehension is a concise way to create a new list by looping over an iterable and optionally applying a condition
# comprehension can be done with lists, sets, and dictionaries. Tuples by default create a generator, must be wrapped
# ------------

# list comprehension
numbers = [ x for x in range(10)]

# set comprehension
unique_fruits = {fruit for fruit in fruits}

# dictionary comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# tuple comprehension
squares_tuple = tuple(x**2 for x in range(5))
