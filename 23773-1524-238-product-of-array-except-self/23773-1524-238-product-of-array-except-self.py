class Solution(object):
    def productExceptSelf(self, nums):
        l = len(nums)
        pre = [1] * l
        suf = [1] * l
        for i in range(1,l):
            pre[i] = pre[i-1] * nums[i-1]
            suf[l-1-i] = suf[l-i] * nums[l-i]
        product = [a * b for a, b in zip(pre, suf)]
        return product