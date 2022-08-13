list = [1, 2, 3, 4, 5, 6, 7]
print("Original list elements:")
print(list)


def removeElement(index):
    del list[index-1]
    print("removing the element: %d" % index)
    print(list)


removeElement(3)
