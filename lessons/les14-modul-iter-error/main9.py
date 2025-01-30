# from itertools import chain
#
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
#
# for x in chain(nums1, nums2):
#     print(x)


gen = (i for i in range(3))
for x in gen:
    print(x)

for x in gen:
    print(x)