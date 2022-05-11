from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s=0
        e=len(nums)-1
        mid = 0
        if nums[s]==target:
            print(0)
        elif nums[e]==target:
            print(e)
        else:
            while s<e:
                mid = (s+e)//2
                if nums[mid]==target:
                    print(mid)
                    break
                elif nums[mid]<target:
                    s= mid+1
                elif nums[mid]>target:
                    e = mid-1
                else:
                    pass
        print(mid+1)
        