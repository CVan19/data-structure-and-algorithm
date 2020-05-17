'''
题目描述：
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

思路：
先对nums进行排序，并按照从左往右递增排列。从头开始依次访问nums的每一个元素。若当前元素<=0，则设置左指针和右指针，分别指向当前元素的下一个元素和nums的最后一个元素，
判断当前元素和两个指针指向的元素的和与0的大小关系；当大于0，则右指针往左移一位；当小于0，则左指针往右移一位；当等于0，则将找到符合要求的一组数，接着向左和向右移动两个指针。
若当前元素>0，则直接访问下一个元素。时间复杂度为O(n2)

防止结果重复的办法：
①在从头开始遍历nums的每一个元素时，若当前元素==上一个元素，则直接访问下一个元素
②在找到一组符合要求的数后，判断两个指针指向的元素是否和下一个位置重复，若重复，则继续往左或往右移


'''



class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []
        nums = sorted(nums)
        result = []
        for i in range(length):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            forward, backward = i + 1, length - 1
            while forward < backward:
                three_sum = nums[i] + nums[forward] + nums[backward]
                if three_sum < 0:
                    forward += 1
                elif three_sum > 0:
                    backward -= 1
                else:
                    result.append([nums[i], nums[forward], nums[backward]])
                    while forward < backward and nums[forward] == nums[forward + 1]:
                        forward += 1
                    while forward < backward and nums[backward] == nums[backward - 1]:
                        backward -= 1
                    forward += 1
                    backward -=1
        return result