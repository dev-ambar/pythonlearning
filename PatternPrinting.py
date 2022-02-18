# for j in range(4):
#     for i in range(4):
#         print("# ",end="")
#     print()


for i in range(8):
    if i < 4:
        for j in range(i + 1):
            print("*", end="")
    else:
        for k in range(8 - i-1):
            print("*", end="")
    print()