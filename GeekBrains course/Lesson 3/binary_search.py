def binary_search(array, value):
    left = 0
    right = len(array) - 1
    pos = (left + right) // 2
    while array[pos]!=value and left<=right:
        if value<array[pos]:
            right = pos - 1
        else:
            left = pos + 1
        pos = (left + right) // 2
    if array[pos] == value:
        return pos
    else:
        return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10], 2))