"""
rows = 3
columns = 4
# Initialize an empty nested list
nested_list = []

# Generate elements and append them to the nested list
for i in range(rows):
    row = []  # Initialize a new row for each iteration
    for j in range(columns):
        # Generate a continuous element based on row and column indices
        element = str(i * columns + j + 1)
        row.append(element)  # Append the element to the current row
    nested_list.append(row)  # Append the row to the nested list

print(nested_list)
"""

# Define the dimensions of the nested list
new_list = []
def nested(new_list):
    nested_list = new_list
    user_inputs = []
    user_input = "a b c"               # input("Enter three numbers separated by spaces: ")
    user_inputs.append(user_input)
    for user_input in user_inputs:
        elements = user_input.split()
        nested_list.append(elements)

    new_list = nested_list

    return nested_list

ret = nested(new_list)
ret = nested(new_list)
ret = nested(new_list)

print(ret)


