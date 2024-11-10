# Initialize the list with some integer values
lista = [1, 2, 8, 4, 15, 20]
max_diff = 0

# Outer loop to iterate through each element starting from the second element
for i in range(1, len(lista)):
    # Inner loop to iterate over all previous elements before the current element at index 'i'
    for j in range(i):
        # Calculate the difference between the element at index 'i' and the element at index 'j'
        if lista[i] - lista[j] > max_diff:
            max_diff = lista[i] - lista[j]

# Print the maximum difference found
print(max_diff)
