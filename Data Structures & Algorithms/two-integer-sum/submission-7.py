class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            tar= target-nums[i]
            if tar in nums:
               for j in range (i+1,len(nums)):
                    if nums[j] == tar:
                        arr.append(i)
                        arr.append(j)
                        return arr
        return arr