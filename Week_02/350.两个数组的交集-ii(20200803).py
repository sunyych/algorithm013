#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Method 1:  Loop throught nums1 and check if it is included in nums2 O(n^2)
        # result = []
        # for num in nums1:
        #     if num in nums2:
        #         result.append(num)
        #         nums2.remove(num)
        # return result

        # Method 2: Hashmap
        hashdict = {}
        result = []
        for num in nums1:
            if num in hashdict:
                hashdict[num] += 1
            else:
                hashdict[num] = 1

        for num in nums2:
            if num in hashdict and hashdict[num] > 0:
                result.append(num)
                hashdict[num] -= 1
        
        return result





# @lc code=end

