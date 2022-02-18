# f = open('MyData', 'r')
# print(f.readline(), end="")
# print(f.readline())
#
# # create a file and write some data
#
# f1 = open('myText', 'w')
# f1.write("I had seen you in last night")

# copy data from pne file to another file
# f = open('MyData', 'r')
# f1 = open('myText', 'w')
# for data in f:
#     f1.write(data)
#
#
# f2 = open('myText', 'r')
# for data in f2:
#     print(data)

# how to read an image or write an image
f = open('LRU.jpg', 'rb')
f1 = open('copy.jpg', 'wb')
for i in f:
    f1.write(i)
