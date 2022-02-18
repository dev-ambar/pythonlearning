pos = -1


def search(lst, s):
    for i in lst:
        if i == s:
            globals()['pos'] = lst.index(i)
            return True
    return False


list = [8, 7, 9, 5, 4, 2]

n = int(input('Enter the search value:->'))

if search(list, n):
    print('found in position ', pos)
else:
    print('not found')
