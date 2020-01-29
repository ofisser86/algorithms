def binary_search(li, item):
    low = 0
    high = len(li) - 1
    count = 0
    while low <= high:
        count += 1
        mid = int((low + high) / 2)
        guess = li[mid]
        if guess == item:
            return f'index of {item}  in list is {mid}. Amount of searches is {count}'
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None

print(binary_search([1, 5, 7, 9, 11, 25, 27, 31, 59], 59))
