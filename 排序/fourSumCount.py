'''
题目描述：
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1 之间，最终结果不会超过 2^31 - 1 。


思路：
利用字典查找时间为O(1)的优势，首先遍历列表A和列表B，找到所有可能的两数之和，并用一个字典记录每一种和出现的次数。然后再分别遍历列表C和列表D，同样找到所有可能的两数之和，
同时查找每一种和对应的相反数在字典中记录的次数并累加，则表示找到多少个这样的元组，使得A[i] + B[j] + C[k] + D[l] = 0。
时间复杂度为O(n^2)，空间复杂度为O(n^2)

'''


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        N = len(A)
        sum_dict = dict()
        for i in range(N):
            for j in range(N):
                add_result = A[i] + B[j]
                sum_dict[add_result] = sum_dict.get(add_result, 0) + 1
        count = 0
        for i in range(N):
            for j in range(N):
                add_result = C[i] + D[j]
                count = count + sum_dict.get(-add_result, 0)
        return count