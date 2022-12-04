with open("day4/input.txt") as f:
    s = 0
    for l in f:
        ranges = l.split(",")
        nums1 = ranges[0].split('-')
        nums2 = ranges[1].split('-')
        if int(nums1[0]) <= int(nums2[0]) and int(nums1[1]) >= int(nums2[1]):
            s += 1
        elif int(nums1[0]) >= int(nums2[0]) and int(nums1[1]) <= int(nums2[1]):
            s += 1
    print(s)

with open("day4/input.txt") as f:
    s = 0
    for l in f:
        ranges = l.split(",")
        nums1 = ranges[0].split('-')
        nums2 = ranges[1].split('-')
        if not (int(nums1[0]) > int(nums2[1]) or int(nums2[0]) > int(nums1[1])):
            s += 1
    print(s)