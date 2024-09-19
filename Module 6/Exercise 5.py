def remove_odd(numbers):
    removed = []
    for num in numbers:
        if num % 2 == 0:
            removed.append(num)
    return removed

full_list = [12,15,22,1,54,55,36,97,121,150,999,1000]
new_list = remove_odd(full_list)

print("The original list:\n", full_list)

print("The new list:\n", new_list)
