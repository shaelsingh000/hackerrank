nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
a = []
if len(nums1)<=len(nums2):
    for i in nums1:
        if i in nums2:
            a.append(i)
else:
    for i in nums2:
        if i in nums1:
            a.append(i)
a = list(set(a))
print(a)