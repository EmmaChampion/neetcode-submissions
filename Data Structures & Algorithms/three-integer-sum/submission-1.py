class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        for start in range(0, len(nums) - 2):
            middle = start + 1
            end = len(nums) - 1
            while middle < end:
                #print(start, middle, end)
                #print(nums[start] + nums[middle] + nums[end])
                if nums[start] + nums[middle] + nums[end] == 0:
                    triple = [nums[start], nums[middle], nums[end]]
                    if triple not in triplets:
                        triplets.append(triple)
                    middle += 1
                    end -= 1
                elif nums[start] + nums[middle] + nums[end] < 0:
                    middle += 1
                else:
                    end -= 1
        return triplets
