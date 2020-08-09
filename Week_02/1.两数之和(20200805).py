#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (49.09%)
# Likes:    8773
# Dislikes: 0
# Total Accepted:    1.3M
# Total Submissions: 2.5M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# 
# 
# 
# 示例:
# 
# 给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力求解，直接算时间复杂度 O(n^2)
        # result = []
        # nums_length = len(nums)
        # for i in range(0, nums_length):
        #     if (i+1) < nums_length:
        #         for j in range(i + 1, nums_length):
        #             if (nums[i] + nums[j]) == target:
        #                 result.append(i)
        #                 result.append(j)
        # return result
        
        #hash
        hashmap = {}

        for idx, num in enumerate(nums):
            hashmap[num] = idx
        for j, num in enumerate(nums): 
            jdx = target - num
            if jdx in hashmap:
                if j != hashmap[jdx]:
                    return [hashmap[jdx], j]


# @lc code=end

