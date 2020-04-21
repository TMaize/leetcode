#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0, 0]
        temp = {}
        start = -1
        for v in nums:
            start += 1
            if temp.get(target - v) == None:
                temp[v] = start
            else:
                result[0] = temp[target - v]
                result[1] = start
        return result


# @lc code=end

s = Solution()
print(s.twoSum([1, 2, 3], 5))
