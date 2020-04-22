#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = 0
        b = 0
        idx = -1
        while l1:
            idx += 1
            a += l1.val * 10**idx
            l1 = l1.next
        idx = -1
        while l2:
            idx += 1
            b += l2.val * 10**idx
            l2 = l2.next
        # python天生支持大数加法运算，无需使用字符串去模拟运算
        s = str(a + b)
        s = s[::-1]

        head = None
        cursor = None
        for i, c in enumerate(s):
            if i == 0:
                head = ListNode(int(c))
                cursor = head
            else:
                cursor.next = ListNode(int(c))
                cursor = cursor.next
        return head


# @lc code=end

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
s = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = s.addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next