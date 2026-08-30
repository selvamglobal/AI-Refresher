# Numeric
## integer, for whole numbers 
count = 5
print(count, type(count));

## float, for decimal numbers
score = 1.2345
print(score, type(score));

## complex, for complex numbers
complex_num = 2 + 3j
print(complex_num, type(complex_num));

# Sequence
## string, for text
name = "Ramesh"
print(name, type(name));

## list, for ordered collections
fruits = ["apple", "banana", "cherry"]
print(fruits, type(fruits));

## tuple, for ordered, immutable collections
coordinates = (10.0, 20.0)
print(coordinates, type(coordinates));

## range, for generating a sequence of numbers
numbers = range(5)
print(list(numbers), type(numbers));

# Mapping
## dictionary, for key-value pairs
person = {"name": "Alice", "age": 30}
print(person, type(person));

# Set
## set, for unordered collections of unique elements
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers, type(unique_numbers));    

## frozenset, for immutable sets
immutable_numbers = frozenset([1, 2, 3, 4, 5])
print(immutable_numbers, type(immutable_numbers));

# Boolean
## bool, for True or False values
is_active = True
print(is_active, type(is_active));

# Binary
## bytes, for immutable sequences of bytes
byte_data = b"Hello"
print(byte_data, type(byte_data));  

# bytearray, for mutable sequences of bytes
mutable_byte_data = bytearray(b"Hello")
print(mutable_byte_data, type(mutable_byte_data));

# memoryview, for viewing the memory of other binary objects
memory_view = memoryview(byte_data)
print(memory_view, type(memory_view));

# dictionary
person = {"name": "Alice", "age": 30}
print(person, type(person));

# NoneType
## NoneType, for representing the absence of a value
none_value = None
print(none_value, type(none_value)); 

# f-string, for formatted string literals
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")   

