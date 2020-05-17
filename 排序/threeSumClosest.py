'''
题目描述：
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

思路：
①对nums进行排序，使其按照升序排列，设置least_delta等于nums的前三个元素和减target的值。
②访问nums的第一个元素x，同时设置左右两个指针分别指向x的下一个元素y和nums的最后一个元素z，计算x+y+z-target的值delta；
③若delta等于0，则直接输出[x, y, z]；若大于0，则右指针往左移一位；若小于0，则左指针往右移一位。
④比较delta的绝对值是否比least_delta的绝对值小，若是，说明x+y+z离target更近，将least_delta更新为delta。
⑤继续比较下一组x,y,z的和与target的差值，重复③④，直至左右两个指针指向同一个元素。
⑥访问nums的下一个元素，重复②③④⑤。直至访问完nums的所有元素。

亮点：
时间复杂度为O(N2)
在访问nums的每一个元素x时，比较能够找到的最大的三数之和与最小的三数之和，与target的差值。若最大的三数之和小于target，或者最小的三数之和大于target，则直接访问nums的下一个元素，不用再设置左右指针。
'''




class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)
        if length < 3:
            return None
        least_delta = nums[0] + nums[1] + nums[2] - target
        for i in range(length - 2):
            delta = nums[i] + nums[i+1] + nums[i+2] - target
            if delta > 0:
                if abs(delta) < abs(least_delta):
                    least_delta = delta
                continue
            delta = nums[i] + nums[length-2] + nums[length-1] - target
            if delta < 0:
                if abs(delta) < abs(least_delta):
                    least_delta = delta
                continue
            forward, backward = i + 1, length - 1
            delta = nums[i] + nums[forward] + nums[backward] - target
            while backward > forward:
                if delta == 0:
                    return target
                elif delta > 0:
                    backward -= 1
                else:
                    forward += 1
                if abs(delta) < abs(least_delta):
                    least_delta = delta
                delta = nums[i] + nums[forward] + nums[backward] - target
        return (target + least_delta)
