from ast import Num
from operator import le
import re
from typing import List


class Solution:
    def searchRange0(self, nums: List[int], target: int) -> List[int]:
        # 解法一：二分查找先随便找到一个目标，然后前后进行遍历
        def binarySearch(nums: List[int], target: int) -> int:
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                elif target < nums[mid]:
                    high = mid
            return None
        loc = binarySearch(nums, target)
        if loc == None:
            return [-1, -1]
        else:
            loc_s = loc_e = loc
            # 向前搜索
            for i in range(loc, -1, -1):
                if nums[i] == target:
                    loc_s = i
            # 后向搜索
            for i in range(loc, len(nums)):
                if nums[i] == target:
                    loc_e = i
            return [loc_s, loc_e]

    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        # 解法二：二分查找先随便找到一个目标，然后前后进行遍历
        def start_loc(nums, target):
            loc_s = -1
            low, high = 0, len(nums)-1  # 左闭右闭
            while low <= high:
                mid = low + (high - low)//2
                if nums[mid] == target:
                    loc_s = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
            return loc_s

        def end_loc(nums, target):
            loc_e = -1
            low, high = 0, len(nums)-1  # 左闭右闭
            while low <= high:
                mid = low + (high - low)//2
                if nums[mid] == target:
                    loc_e = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
            return loc_e
        loc_s,loc_e = start_loc(nums, target), end_loc(nums, target)
        return [loc_s,loc_e]


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange1([5, 7, 7, 9, 10, 10], 7))
