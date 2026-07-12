class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeroes = 0
        total_prod = 1
        for num in nums:
            if num == 0:
                num_zeroes += 1
            else:
                total_prod *= num
        
        products = []
        if num_zeroes > 1:
            products = [0] * len(nums)
        elif num_zeroes == 1:
            for num in nums:
                if num == 0:
                    products.append(total_prod)
                else:
                    products.append(0)
        else:
            for num in nums:
                products.append(total_prod // num)
        
        return products
