def sort(lst):
    ln = len(lst) - 1
    while ln > 0:
        for j in range(ln):
            if lst[j] > lst[j + 1]:
                temp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = temp
        # print(lst)
        ln -= 1
    return lst


lst = [8, 2, 5, 100, 3, 78, 9, 1]

print("lst is in unsorted order:->", lst)

lst = sort(lst)

print("lst is in sorted order:->", lst)
