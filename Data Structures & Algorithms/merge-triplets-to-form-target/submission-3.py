class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid0 = False
        valid1 = False
        valid2 = False
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            if not valid0 and triplet[0] == target[0]:
                valid0 = True
            if not valid1 and triplet[1] == target[1]:
                valid1 = True
            if not valid2 and triplet[2] == target[2]:
                valid2 = True
        return valid0 and valid1 and valid2