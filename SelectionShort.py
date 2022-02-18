def sort(lst):
    for i in range(len(lst) - 1):
        minPos = i
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
                minPos = j
    return lst


lst = [8, 2, 5, 100, 3, 78, 9, 1]

print("lst is in unsorted order:->", lst)

lst = sort(lst)

print("lst is in sorted order:->", lst)
