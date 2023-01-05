from typing import List


class Solution:
    def searchInsert_0(self, nums: List[int], target: int) -> int:
        # 左闭右闭,注意赋初值时high的取值
        low, high = 0, len(nums) - 1 
        while low <= high: 
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
        # 如果数组里没找到target，那么low会比high大，而此时low的位置就是target位置
        return low 
    def searchInsert_1(self, nums: List[int], target: int) -> int:
        # 左闭右开,注意赋初值时high的取值
        low, high = 0, len(nums)
        while low < high: 
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif target < nums[mid]:
                high = mid
        # 如果数组里没找到target，最后一步走的是nums[mid] < target，所以此时low就指的targetr位置
        return low 