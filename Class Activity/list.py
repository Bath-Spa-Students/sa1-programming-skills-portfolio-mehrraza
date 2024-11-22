# They may differ in type or be homogenous (of the same kind).
# Example of a Homogeneous List
colors = ["Black", "Blue", "Green"]
print(colors)

# Heterogeneous List Illustration
outline = ["Ahmad", 19, True]
print(outline)

# To replicate elements in a list, use the repetition operator (*).
information = [0, 0, 1]
duplicated_information= information * 3
print(duplicated_information)

# Positive Indexing: Use non-negative integers to access list elements
information = [5, 10, 15, 20, 25]
print(information[4])  # Access element at index 4

# Negative Indexing: List items beginning with -1
information = [10, 20, 30, 40, 50]
print(information[-1])  # Access the last element

# `len()`: Returns the total number of elements in a list
information = [5, 10, 15, 20]
print("Length of the list:", len(information))

# Lists are mutable, meaning their contents can be changed
information[2] = 99  # Updating the third element
print(information)

# Concatenation: Merging two lists using `+`
alpha = ["A", "B", "C"]
numeric = [1, 2, 3]
combined = alpha + numeric
print(combined)

# Slicing: Extracting a subset of a list
characters = ["a", "b", "c", "d", "e", "f"]
subset = characters[2:5]  # Extract elements from index 2 to 4
print(subset)

# `in` operator: Check if an element exists in a list
if "b" in characters:
    print("Found 'b'")
else:
    print("'b' not found")

# `not in` operator: Verify if an element is absent in a list
if "z" not in characters:
    print("'z' is not in the list")

# Built-in List Methods

# `append()`: Add an element at the end
characters.append("g")
print(characters)

# `index()`: Determine an element's index
print("Index of 'c':",characters.index("c"))

# `sort()`: Put items in ascending sequence
figures = [9, 3, 7, 2]
figures.sort()
print("Sorted list:", figures)

# `reverse()`: Flip the list's order
figures.reverse()
print("Reversed list:", figures)

# `remove()`: Eliminate an element's first appearance
figures.remove(7)
print("After removal:", figures)

# Get the maximum and minimum values using `max()` and `min()`
print("Maximum:", max(figures))
print("Minimum:", min(figures))
