#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (76.66%)
# Likes:    842
# Dislikes: 0
# Total Accepted:    172.1K
# Total Submissions: 224.5K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # recursion terminator
        if len(nums) <= 1:
            return [nums]
        
        # process logic in current level
        res = []
        for idx, num in enumerate(nums):
            res_nums = nums[:idx] + nums[idx + 1:]  # 确定剩余元素
            
            # drill down
            for j in self.permute(res_nums):  
                res.append([num] + j)
        return res



# @lc code=end

