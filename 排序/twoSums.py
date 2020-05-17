'''
题目描述：
给定一个整数数组nums和目标值target， 在数组中找出和为目标值的两个整数，并且返回它们的下标。假设每个目标值只对应一个答案。

思路一：
用一个与nums同等长度的数组rawIndex在对应位置上记录nums中每一个数字的索引，在对nums进行快速排序的同时，相应地移动每个数字对应的索引。
排序后，用头指针和尾指针分别指向nums的头部和尾部，将两个指针对应的数字相加；若和大于target，则将指向尾指针向前移一位；若和小于target，则将头指针向前移一位；若等于，则返回两个指针对应的数字的索引。
时间复杂度为O(nlogn)，空间复杂度为O(n)

思路二：
利用哈希表快速定址的优势，将nums的每个元素与对应的索引存在哈希表中，元素为键，索引为值。遍历nums，检查target-element是否存在于字典中，从而实现O(n)的时间复杂度，空间复杂度为O(n)
'''



def quickSort(nums, start, end, rawIndex):
        if end == start or end < start:
            return
        pivot = nums[start]
        forward, backawrd = start + 1, end
        while True:
            if forward == backawrd:
                if nums[forward] <= pivot:
                    nums[start] = nums[forward]
                    nums[forward] = pivot
                    tmp = rawIndex[start]
                    rawIndex[start] = rawIndex[forward]
                    rawIndex[forward] = tmp
                else:
                    backawrd -= 1
                break
            while nums[backawrd] > pivot and backawrd > forward:
                backawrd -= 1
            while nums[forward] <= pivot and forward < backawrd:
                forward += 1
            if forward == backawrd:
                continue
            tmp = nums[forward]
            nums[forward] = nums[backawrd]
            nums[backawrd] = tmp
            tmp = rawIndex[forward]
            rawIndex[forward] = rawIndex[backawrd]
            rawIndex[backawrd] = tmp
        quickSort(nums, start, forward - 1, rawIndex)
        quickSort(nums, backawrd + 1, end, rawIndex)

#排序法
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rawIndex = [i for i in range(len(nums))] #各个数字未排序前的索引
        forward, backawrd = 0, len(nums) - 1
        quickSort(nums, 0, backawrd, rawIndex)
        sumResult = nums[forward] + nums[backawrd]
        while sumResult != target:
            if sumResult > target:
                backawrd -= 1
            else:
                forward += 1
            sumResult = nums[forward] + nums[backawrd]
        return [rawIndex[forward], rawIndex[backawrd]]
        
#字典法
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, element in enumerate(nums):
            left = target - element
            if left in hashmap:
                return [index, hashmap[left]]
            hashmap[element] = index
