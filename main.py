def search(value, data):
    middle = round(len(data) / 2)  # The middle point is an index
    if data[middle] == value:  # Base case
        return middle

    left = []
    idx = 0
    # Contructing the left side of middle
    while not data[idx] == data[middle]:
        left.append(data[idx])
        idx += 1

    # Right side is equal to the whole data set
    right = data[:]
    # Removing the left side so only the right side remains
    for i in range(len(left)):
        right.remove(left[i])

    # Checking where value is and calling the function again
    if value in left:
        return search(value, left)
    elif value in right:
        return middle + search(value, right)
