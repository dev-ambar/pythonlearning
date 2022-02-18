pos = -1


def search(lst, s):
    lb = 0
    ub = len(lst) - 1
    while lb <= ub:
        m = (lb + ub) // 2
        if lst[m] == s:
            globals()['pos'] = m
            return True
        else:
            if lst[m] < s:
                lb = m + 1
            else:
                ub = m - 1
    return False


lt = [2, 4, 5, 8, 9, 11, 99, 1458, 1658, 9999]

n = int(input('Enter the search value:->'))
if search(lt, n):
    print('found in position ', pos + 1)
else:
    print('not found')
