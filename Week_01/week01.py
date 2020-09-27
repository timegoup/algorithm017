移动零（https://leetcode-cn.com/problems/move-zeroes/submissions/）
第一次写的代码： 删除一个零在后面补充一个零
class Solution(object):
    def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """ 
        for i in nums:
            if i == 0:
            nums.remove(i)
            nums.append(0)
        return nums
优秀案例： 两个变量，一个变量标记遍历的位置，一个标记当前是零的位置
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # if not nums:
    # return 0
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j]=nums[j],nums[i]
                j+=1
        return nums


盛水最多水的容器（https://leetcode-cn.com/problems/container-with-most-water/）：
暴力破解： 遍历所有的面积，找到其中最大的
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                Area = (j-i) * min(height[i],height[j])
                maxArea = max(Area, maxArea)
            return maxArea
优秀案例：从两端移动，最小的往前移动才有可能取到大的值
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height)-1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j-i))
                i+=1
            else:
                res = max(res, height[j] * (j-i))
                j-=1
            return res

 