'''
题目描述：
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
    输入:nums = [1,1,1], k = 2
    输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

思路：
设sum[i]表示nums的下标从0到i的元素的累积和，假如sum[i] - sum[j]等于k，表示下标从j+1到i的连续子数组的和为k。
按照这个思路，从左往右计算nums每一项的累积和s，并用一个哈希表来记录s出现的次数，判断s-k是否为哈希表的键。
若是，则表明找到了以当前项为最后一个元素的连续子数组，它的和为k。这样的连续子数组有多少个，则取决于s-k出现的次数。据此更新count。

易错：
在初始化哈希表时，要设置累积和0出现的次数为1。这样可防止当累积和为7时被漏算。

'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        L = len(nums)
        hashtable = {0:1}
        count = 0
        accumulated_sum = 0
        for i in range(L):
            accumulated_sum += nums[i]
            left = accumulated_sum - k
            if left in hashtable:
                count += hashtable[left]
            if accumulated_sum in hashtable:
                hashtable[accumulated_sum] += 1
            else:
                hashtable[accumulated_sum] = 1
        return count