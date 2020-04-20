'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
注意，答案中不可以包含重复的四元组

思路：
与三数之和类似，只不过在外面多嵌套了一层循环，复杂度为O(n3)

亮点：
在每次循环前，判断当前范围内四个数相加和的最小值与最大值和target的大小关系，能减少大量不不必要的循环次数

'''



class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 4:
            return []
        result = []
        nums = sorted(nums)
        for k  in range(length - 3):
            if nums[k] + nums[k+1] + nums[k+2] + nums[k+3] > target:
                break
            if nums[k] + nums[length-1] + nums[length-2] + nums[length-3] < target:
                continue
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            for i in range(k+1, length - 2):
                if nums[k] + nums[i] + nums[i+1] + nums[i+2] > target:
                    break
                if nums[k] + nums[i] + nums[length-1] + nums[length-2] < target:
                    continue
                if i > k + 1 and nums[i] == nums[i - 1]:
                    continue
                forward, backward = i + 1, length - 1
                while forward < backward:
                    four_sum = nums[k] + nums[i] + nums[forward] + nums[backward]
                    if four_sum < target:
                        forward += 1
                    elif four_sum > target:
                        backward -= 1
                    else:
                        result.append([nums[k], nums[i], nums[forward], nums[backward]])
                        while forward < backward and nums[forward] == nums[forward + 1]:
                            forward += 1
                        while forward < backward and nums[backward] == nums[backward - 1]:
                            backward -= 1
                        forward += 1
                        backward -= 1
        return result