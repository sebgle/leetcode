# Last updated: 7/16/2025, 9:42:45 AM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextg = {}
        answer = [0] * len(nums1)
        for num in nums2:
            while len(stack) > 0 and stack[-1] < num:
                val = stack.pop()
                nextg[val] = num
            stack.append(num)
        while len(stack) > 0:
            val = stack.pop()
            nextg[val] = -1
        for i in range(len(nums1)):
            answer[i] = nextg[nums1[i]]
        return answer