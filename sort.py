# Built in
list1 = [1, 2, 0, 3]
list1.sort()
print(list1)

# using lambda
x = lambda list3: sorted(list3)
print(x([1, 0, 6, 5, 2]))
# Traditional way
list2 = [1, 0, 3, 2, 5, 4]
for i in range(len(list2) - 1):

    for j in range(0, len(list2) - i - 1):

        if list2[j] > list2[j + 1]:
            list2[j], list2[j + 1] = list2[j + 1], list2[j]

print(list2)
